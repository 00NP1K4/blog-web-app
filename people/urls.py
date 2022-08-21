from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('post/<slug:slug>/', post, name="post_detail"),
    path('category/<int:id>/', categories, name="category"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('all/', all_post, name="all"),
]
