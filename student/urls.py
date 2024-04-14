from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('', views.index),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]