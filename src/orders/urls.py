from django.views.generic.base import View

from django.urls import path

from . import views


app_name = 'orders'
urlpatterns = [
    path(
        'delete-book-in-cart/<int:pk>', 
        views.DeleteBookInCart.as_view(), 
        name='book-in-cart-del'
    ),
    path('update-caer', views.CartUpdateView.as_view(), name='update'),
    path('', views.CartView.as_view(), name='cart')
    
]