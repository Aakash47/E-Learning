from django.urls import path
from . import views
from user.views import blogpost
from courses.views import coursePage

urlpatterns = [
    path('book/', views.book, name="book"),
    path('merch/', views.merch, name="merch"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('store/<slug:slug>/', views.storeview, name='storeview'),
    path('user_order/', views.user_order, name = 'user_order'),
    path('cart_verify_payment', views.verifyPayment , name = 'cart_verify_payment'),
]
