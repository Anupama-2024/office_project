from django.urls import path 
from . import views


urlpatterns = [
    path('', views.office_list, name='office_list'),
    path('create/', views.office_create, name='office_create'),
    path('update/<int:pk>/', views.office_update, name='office_update'),  
    path('delete/<int:pk>/', views.office_delete, name='office_delete'),
]
