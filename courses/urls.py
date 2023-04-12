from django.urls import path, include
from . import views

urlpatterns = [
    path('courses/', views.courses, name="courses"),
    path('courses/<slug:slug>/', views.coursePage, name='coursePage'),
    path('check-out/<slug:slug>/', views.checkout , name = 'check-out'),
    path('my_courses/', views.my_courses , name = 'my_courses'),
    path('verify_payment', views.verifyPayment , name = 'verify_payment'),
    
]