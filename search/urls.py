from django.urls import path
from . import views

urlpatterns = [
    path('getpost', views.GetPost.as_view()),
    path('getposts', views.GetPosts.as_view()),
    path('upload', views.Upload.as_view()),
    path('poststuff', views.PostStuff.as_view()),
    path('getpost/<slug:slug>', views.GetPost.as_view()),
    path('remove/<slug:slug>', views.RemovePicture.as_view()),
]