from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def store(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request, 'store/store.html', context)

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}


def list_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/list-category.html', {'category': category, 'products': products})


def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'store/product-info.html', context)

