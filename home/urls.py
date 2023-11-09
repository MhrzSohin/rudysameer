from .views import *
from django.urls import path

urlpatterns = [
    path("",HomeView.as_view(), name='home'),
    path('cart',CartView.as_view(), name='cart'),
    path("category/<slug>",CategoryView.as_view(), name = 'category'),
    path('shop',ShopView.as_view(), name='shop'),
    path('search',SearchView.as_view(), name='search'),
    path('signup',signup, name='signup'),
    path("detail/<slug>", DetailView.as_view(), name='detail'),
    path('add_to_cart/<slug>',cart, name='add_to_cart'),
    path('reduce_quantity/<slug>', reduce_quantity, name='reduce_quantity'),
    path('delete_cart/<slug>',delete_cart, name='delete_cart'),
    path('submit_review/<slug>',submit_review, name='submit_review'),
    path('checkout', checkout, name='checkout'),
]
