from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ItemsList, ItemsDetail

# app_name="items"

urlpatterns = [
  path('', views.index, name="index"),
  path('register', views.register, name="register"),
  path('items_list', ItemsList.as_view(), name="items_list"),
  path('detail/<int:pk>', ItemsDetail.as_view()),
  path('edit/<int:num>', views.edit, name="edit"),
  path('delete/<int:num>', views.delete, name="delete"),
]
