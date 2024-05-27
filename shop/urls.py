
from django.urls import path
from .views import ClientListAPIView, ContactApplicationCreateView

urlpatterns = [
    path('clients/', ClientListAPIView.as_view()),
    path('contact/', ContactApplicationCreateView.as_view()),

]
