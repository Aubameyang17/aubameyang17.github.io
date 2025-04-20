from django.urls import path
from recruto_test import views

urlpatterns = [
    path("", views.index),
    path("user/", views.user)
]