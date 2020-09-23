from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.Home, name="home"),
    path('create/', views.newcreate, name="create"),
    path('update/<int:pk>/',views.newsupdate, name="update"),
    path('delete/<int:pk>/', views.newsdelete, name="delete")
]

