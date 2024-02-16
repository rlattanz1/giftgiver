from django.urls import path
from . import views



urlpatterns = [
    # path(route you need to go to, view you need to render, a name to allow you to dynammically access it)
    path('', views.getRoutes, name='routes'),
    path('gifts/', views.getGifts, name='gifts'),
    path('gifts/<str:pk>/', views.getGift, name='gift'),
]
