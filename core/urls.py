from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('borrowed_list', views.borrowed_list, name='borrowed_list'),
    path('items_list', views.items_list, name='items_list'),
    path('workers_list', views.workers_list, name='workers_list'),
    path('new_worker', views.CreateWorker.as_view(), name='create_worker'),
    path('update_worker/<int:pk>', views.UpdateWorker.as_view(), name='update_worker'),
    path('delete_worker/<int:pk>', views.DeleteWorker.as_view(), name='delete_worker')
]
