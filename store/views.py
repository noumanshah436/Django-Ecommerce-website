from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


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
