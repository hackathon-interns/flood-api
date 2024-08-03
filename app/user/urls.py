from django.urls import path, include
from user import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', views.UserView.as_view(), name='user'),
]
