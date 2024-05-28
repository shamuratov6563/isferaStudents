from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Discount,Faq
from .serializers import DiscountSerializer,FrequentlyAskedQuestionsSerializer

class DiscountListView(ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class DiscountCreateAPIView(CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class FaqListView(ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FrequentlyAskedQuestionsSerializer

class FaqCreateAPIView(CreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FrequentlyAskedQuestionsSerializer
