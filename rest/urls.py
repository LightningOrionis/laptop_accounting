from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('borrowed_items', views.BorrowedItemsListView.as_view(), name='borrowed_items_list_api'),
    path('workers', views.WorkersListView.as_view(), name='workers_list_api'),
    path('all_items', views.AllItemsListView.as_view(), name='all_items_list_api'),
    path('unborrowed_items', views.UnborrowedItemsListView.as_view(), name='unborrowed_items_list_api'),
    path('borrowed_item/<int:pk>', views.BorrowedItemDetailView.as_view(), name='borrowed-item-detail-api'),
    path('worker/<int:pk>', views.WorkerDetailView.as_view(), name='worker-detail-api'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail-api'),
]
