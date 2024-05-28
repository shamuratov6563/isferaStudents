from django.urls import path
from shop import views 

urlpatterns = [
    path('discount-list/', views.DiscountListView.as_view()),
    path('discount-create/', views.DiscountCreateAPIView.as_view()),

    path('faq-list/', views.FaqListView.as_view()),
    path('faq-create/', views.FaqCreateAPIView.as_view()),

]