from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('borrowed_list', views.borrowed_list, name='borrowed_list'),
    path('items_list', views.items_list, name='items_list'),
    path('workers_list', views.workers_list, name='workers_list'),
    path('new_worker', views.CreateWorker.as_view(), name='create_worker'),
    path('worker/<int:pk>/update', views.UpdateWorker.as_view(), name='update_worker'),
    path('worker/<int:pk>/delete', views.DeleteWorker.as_view(), name='delete_worker'),
    path('worker/<int:pk>', views.worker_detail, name='worker_detail'),
    path('new_item', views.CreateItem.as_view(), name='create_item'),
    path('item/<int:pk>/update', views.UpdateItem.as_view(), name='update_item'),
    path('item/<int:pk>/delete', views.DeleteItem.as_view(), name='delete_item'),
    path('item/<str:id>/borrow', views.BorrowItem.as_view(), name='borrow_item'),
    path('borrowed_item/<int:pk>/return', views.ReturnItem.as_view(), name='return_item'),
]
