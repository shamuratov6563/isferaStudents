from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ClientListAPIView, ContactApplicationCreateView,ProductfilterListView


urlpatterns = [
    path('product-list/', views.ProductListAPIView.as_view()),
    path('caregory-list/', views.CategoryListAPIView.as_view()),
    path('clients/', ClientListAPIView.as_view()),
    path('contact/', ContactApplicationCreateView.as_view()),
    path('discount-list/', views.DiscountListView.as_view()),
    path('faq-list/', views.FaqListView.as_view()),
    path('product-filter-list/', views.ProductfilterListView.as_view()),  
]

