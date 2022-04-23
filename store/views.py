from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import ProductForm


# Create your views here.

def home(request):
    return render(request, 'store/index.html')


def collections(request):
    categories = Category.objects.filter(status=0)
    context = {'categories': categories}
    return render(request, 'store/collections.html', context)


def collectionsViews(request, slug):
    # check if the category exist with that slug or not
    if Category.objects.filter(slug=slug, status=0):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        # using foreign key get all products with the slug category match
        context = {'products': products, 'category': category}
        return render(request, 'store/products/index.html', context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')


#  what you mention in the url should be passed over here
def productViews(request, cate_slug, prod_slug):
    if Category.objects.filter(slug=cate_slug, status=0):
        if Product.objects.filter(slug=prod_slug, status=0):
            product = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'product': product}
        else:
            messages.warning(request, "No such Product found")
            return redirect('collections')
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')
    return render(request, 'store/products/view.html', context)


# http://127.0.0.1:8000/addProduct
def addProduct(request):
    if request.method == "POST":
        fm = ProductForm(request.POST, request.FILES)
        if fm.is_valid():
            product = fm.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('collections')
    else:
        fm = ProductForm()
    return render(request, 'store/addProduct.html', {'form': fm})


# This funcion will update/edit
def updateProduct(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        fm = ProductForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('collections')
    else:
        pi = Product.objects.get(pk=id)
        fm = ProductForm(instance=pi)
    return render(request, 'store/updateProduct.html', {'form': fm})


def deleteProduct(request, id):
    if request.method == 'POST':
        product = Product.objects.get(pk=id)
        product.delete()
        return redirect('collections')
