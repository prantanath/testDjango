from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('add_std',views.add_std,name="add_std"),
    path('view_std',views.view_std,name="view_std"),
    path('update/<id>',views.edit_std,name="edit_std"),
    path('delete/<id>',views.delete,name="delete")
]
