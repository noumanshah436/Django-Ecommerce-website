from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    return render(request, 'store/index.html')


def collections(request):
    categories = Category.objects.filter(status=0)
    context = {'categories': categories}
    return render(request, 'store/collections.html', context)
