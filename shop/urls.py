from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ClientListAPIView, ContactApplicationCreateView, StatiyListView,RepairAppCreateAPIView,ProductDetailAPIView


urlpatterns = [
    path('faq-list/', views.FaqListView.as_view() ),
    path('prduct-repair/', views.ProductListAPIView.as_view()),
    path('category-list/', views.CategoryListAPIView.as_view()),
    path('category-with-image/', views.CategoryListWithImage.as_view()),
    path('clients/', ClientListAPIView.as_view()),
    path('contact/', ContactApplicationCreateView.as_view()),
    path('repair-app/', RepairAppCreateAPIView.as_view()),

    path('discount-list/', views.DiscountListView.as_view()),
    path('discount-create/', views.DiscountCreateAPIView.as_view()),
    path('faq-create/', views.FaqCreateAPIView.as_view()),
    path('statiy-list/', StatiyListView.as_view()),
    path('statiy-list/detail/<int:pk>', StatiyListView.as_view()),
    path('email-create/', views.EmailCreateView.as_view()),

    path('products/', views.ProductListAPIView.as_view()),
    path('products-detail/<int:pk>', views.ProductDetailAPIView.as_view())

]

