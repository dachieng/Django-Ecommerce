from django.shortcuts import render,get_object_or_404
from store.models import Category, Product

def products(request):
    products = Product.objects.all()
    return render(request, "store/home.html", {"products" : products})

def categories(request):
    return {
        "categories" : Category.objects.all()
    }

def product_detail(request, slug):
    product = get_object_or_404(Product,slug=slug)
    return render(request, "store/product_detail.html", {"product" : product})

def category_list(request,slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request,"store/categories.html", {"products":products, "category" : category})