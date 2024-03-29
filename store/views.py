from django.shortcuts import render
from .models import Category,Product
from django.shortcuts import get_object_or_404
from django.urls import reverse
# Create your views here.
def store(request):
    all_products=Product.objects.all()
    context={'all_products':all_products}
    return render(request,'store/store.html',context=context)

def categories(request):
    all_categories=Category.objects.all()
    return {'all_categories':all_categories}

def list_category(request,slug):
    category=Category.objects.get(slug=slug)
    products=Product.objects.filter(category=category)
    return render(request,'store/list-category.html',{'category':category,'products':products})

def product_info(request,slug):
    product=Product.objects.get(slug=slug)
    context={'product':product}
    return render(request,'store/product-info.html',context=context)

