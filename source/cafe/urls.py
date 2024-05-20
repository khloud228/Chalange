from django.urls import path

from .views import (
    RegisterView,
    CategoryView,
    ProductView,
    
    ProductByCategory
)


urlpatterns = [
    path('user/signup/', RegisterView.as_view()),
    path('category/all/', CategoryView.as_view()),
    path('product/all/', ProductView.as_view()),
    path('product/category/<slug:cat_slug>', ProductByCategory.as_view())
]
