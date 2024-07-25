from django.urls import path
from . import views


app_name = 'video'

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('search',views.search, name='search'),
]