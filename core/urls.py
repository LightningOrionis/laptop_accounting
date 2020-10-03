from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('borrowed_list', views.BorrowedItemsListView.as_view(), name='borrowed_list'),
    path('items_list', views.ItemsListView.as_view(), name='items_list'),
    path('workers_list', views.WorkersListView.as_view(), name='workers_list'),
    path('new_worker', views.CreateWorkerView.as_view(), name='create_worker'),
    path('worker/<int:pk>/update', views.UpdateWorkerView.as_view(), name='update_worker'),
    path('worker/<int:pk>/delete', views.DeleteWorkerView.as_view(), name='delete_worker'),
    path('worker/<int:pk>', views.WorkerDetailView.as_view(), name='worker_detail'),
    path('new_item', views.CreateItemView.as_view(), name='create_item'),
    path('item/<int:pk>/update', views.UpdateItemView.as_view(), name='update_item'),
    path('item/<int:pk>/delete', views.DeleteItemView.as_view(), name='delete_item'),
    path('item/<str:id>/borrow', views.BorrowItemView.as_view(), name='borrow_item'),
    path('borrowed_item/<int:pk>/return', views.ReturnItemView.as_view(), name='return_item'),
]
