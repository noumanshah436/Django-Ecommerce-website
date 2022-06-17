from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.forms import CustomUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from store.models import Product, Cart


def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully!")
            return redirect('/login')

    context = {'form': form}
    return render(request, "users/register.html", context)


@login_required
def profile(request):
    if request.method == 'POST':
        print("request.user :", request.user)
        print("request.user.profile :", request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,  # to populate/get the updated post data into the fields
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


# def LoginPage(request):
#     if request.user.is_authenticated:
#         messages.warning(request, "You are already logged in!")
#         return redirect('/')
#     else:
#         if request.method == 'POST':
#             name = request.POST.get('username')
#             password = request.POST.get('password')
#
#             user = authenticate(request, username=name, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "Login Successful!")
#                 return redirect('/')
#             else:
#                 messages.success(request, "Invalid Login or password!")
#                 return redirect('login')
#         return render(request, "users/login.html")


# def LogoutPage(request):
#     if request.user.is_authenticated:
#         logout(request)
#         messages.warning(request, "Logged out sccessfully!")
#     return redirect('/')


def addToCart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)

            if product_check:
                if Cart.objects.filter(user=request.user.id, product_id=prod_id):
                    return JsonResponse({'status': 'Product Already in Cart'})
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        messages.success(request, f'Product Added to Cart Successfully!')
                        return redirect('/')

                        # return JsonResponse({'status': 'Product Added Successfully'})
                    else:
                        return JsonResponse({'status': "only" + str(product_check.quantity) + "quantity available"})
            else:
                return JsonResponse({'status': 'No Such Product Found'})
        else:
            return JsonResponse({'status': 'Login to continue'})

    return redirect('/')

@login_required
def viewCart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {"cart": cart}
    return render(request, 'users/cart.html', context)


def updateCart(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        if Cart.objects.filter(user=request.user.id, product_id=prod_id):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(user=request.user, product_id=prod_id)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status': 'Updated Successfully'})
    return redirect('/')

def deleteCart(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        if Cart.objects.filter(user=request.user.id, product_id=prod_id):
            cartItem = Cart.objects.get(user=request.user, product_id=prod_id)
            cartItem.delete()
            return redirect('cart')
            # return JsonResponse({'status': 'Deleted Successfully'})
    return redirect('/')
