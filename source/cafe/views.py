from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .serializers import (
    RegisterSerializer,
    UserSerializer,
    RuTagSerializer,
    ProductSerializer
)
from .models import RuTag, Product
from source.services import CustomPageNumberPagination


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "message": "Пользователь успешно создан",
            "user": UserSerializer(instance=user).data,
        })


class CategoryView(ListAPIView):
    serializer_class = RuTagSerializer
    queryset = RuTag.objects.all()
    permission_classes = (AllowAny,)


class ProductView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = CustomPageNumberPagination


class ProductByCategory(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        category_slug = self.kwargs['cat_slug']
        products = Product.objects.filter(categories__slug=category_slug)
        return products
