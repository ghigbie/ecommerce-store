from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    # path('product/<slug:slug>', views.product_info, name='product-info'),
    # path('search/<slug:slug>', views.list_category, name='list-category'),
]
