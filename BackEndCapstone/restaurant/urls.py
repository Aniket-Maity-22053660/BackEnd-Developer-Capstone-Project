#define URL route for index() view
from django.urls import path, include
from . import views

urlpatterns = [
    path('view/', views.index, name='index'),
    path('items/', views.MenuView.as_view(), name='menu'),
    path('items/<int:pk>/', views.SingleMenuView.as_view(), name='single-menu'),

]
