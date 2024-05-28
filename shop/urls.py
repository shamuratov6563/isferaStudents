from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('faq-list/', views.FAQListAPIView.as_view() ),
    path('product-list/', views.ProductListAPIView.as_view()),
    path('caregory-list/', views.CategoryListAPIView.as_view())
]
