from django.urls import path
from .views import testCart


urlpatterns = [
    path('', testCart),
]
