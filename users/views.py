from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.forms import CustomUserForm
from django.contrib.auth.decorators import login_required


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
    return render(request, 'users/profile.html')

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
