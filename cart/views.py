from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
    context = {}
    return render(request, 'cart/cart-summary.html', context)


def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty=product_quantity)
        cart_quantity = cart.__len__()
        response = JsonResponse({'name': product.title, 'qty': cart_quantity, 'price': product.price})
        return response


def cart_delete(request):
    pass


def cart_update(request):
    pass
