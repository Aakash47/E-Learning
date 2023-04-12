from django.urls import path, include
from . import views

urlpatterns = [
    path('freelance/', views.freelance, name='freelance'),
    # path('contact_freelancer/', views.contfreelancer, name='contfreelancer'),
    path('freelance/<slug:slug>/', views.freelancepage, name='freelancepage'),
]
