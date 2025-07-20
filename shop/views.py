from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})