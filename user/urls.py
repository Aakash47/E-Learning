from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('blog/', views.blog, name='Blog'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('blog/<slug:post>/', views.blogpost, name='Blogpost'),
    
]