from django.urls import path

from .views import viewCart, addToCart,remFromCart


urlpatterns = [
    path('cart/', viewCart, name = 'view_cart'),
    path('cart/add/<int:product_id>', addToCart, name = 'add_to_cart'),
    path('cart/rem/<int:cart_item_id>', remFromCart, name = 'rem_from_cart')
]