from django.urls import path

from .views import RegisterView


urlpatterns = [
    path('user/signup/', RegisterView.as_view()),
]
