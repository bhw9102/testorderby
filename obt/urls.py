from django.contrib import admin
from django.urls import path, include
from obt import views


urlpatterns = [
    path('list/case_1/', views.list_view_case_1, name='list_view_case_1'),
    path('list/case_2/', views.list_view_case_2, name='list_view_case_2'),
]

