from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('sign-up', views.sign_up, name='sign_up'),
    path('contact', views.contact, name="contact"),
    path('shop', views.shop, name="shop"),
]