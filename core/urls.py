from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('borrowed_list', login_required(views.BorrowedItemsListView.as_view()), name='borrowed_list'),
    path('items_list', login_required(views.ItemsListView.as_view()), name='items_list'),
    path('workers_list', login_required(views.WorkersListView.as_view()), name='workers_list'),
    path('new_worker', login_required(views.CreateWorkerView.as_view()), name='create_worker'),
    path('worker/<int:pk>/update', login_required(views.UpdateWorkerView.as_view()), name='update_worker'),
    path('worker/<int:pk>/delete', login_required(views.DeleteWorkerView.as_view()), name='delete_worker'),
    path('worker/<int:pk>', login_required(views.WorkerDetailView.as_view()), name='worker_detail'),
    path('new_item', login_required(views.CreateItemView.as_view()), name='create_item'),
    path('item/<int:pk>/update', login_required(views.UpdateItemView.as_view()), name='update_item'),
    path('item/<int:pk>/delete', login_required(views.DeleteItemView.as_view()), name='delete_item'),
    path('item/<str:id>/borrow', login_required(views.BorrowItemView.as_view()), name='borrow_item'),
    path('borrowed_item/<int:pk>/return', login_required(views.ReturnItemView.as_view()), name='return_item'),
    path('accounts/', include("django.contrib.auth.urls"))
]
