from django.urls import path, include
from . import views

urlpatterns = [
    path('creater/', views.sellerorder, name="creater"),    
    path('addblog/', views.addblog, name="addblog"),    
    path('addcourse/', views.addcourse, name="addcourse"),  
    path('addproduct/', views.addproduct, name="addproduct"),  
    path('addfreelance/', views.addfreelance, name="addfreelance"),  
    path('createrblogs/', views.createrblog, name="createrblogs"),  
    path('creatercourse/', views.creatercourse, name="creatercourse"),  
    path('createrproducts/', views.createrproduct, name="createrproducts"),  
    path('createrfreelances/', views.createrfreelance, name="createrfreelances"),  
    path('post/update/<slug:post>/', views.updateblogs, name="updateblog"),  
    path('post/delete/<slug:post>/', views.deleteblog, name="deleteblog"),  
    path('course/update/<slug:slug>/', views.updatecourse, name="updatecourse"),  
    path('product/update/<slug:slug>/', views.updateproduct, name="updateproduct"),  
    path('freelance/update/<slug:slug>/', views.updatefreelance, name="updatefreelance"),  
]