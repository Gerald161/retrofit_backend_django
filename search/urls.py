from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.Upload.as_view()),
    path('remove/<slug:slug>', views.RemovePicture.as_view()),
]