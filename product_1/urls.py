from django.urls import path
from . import views

urlpatters = [
    path('', views.home_page(), name='home_page_url'),
]