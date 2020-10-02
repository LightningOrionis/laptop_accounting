from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from core.models import *

from .serializers import *


class BorrowedItemsListView(generics.ListCreateAPIView):
    model = BorrowedItem
    serializer_class = BorrowedItemSerializer

    def get_queryset(self):
        return BorrowedItem.objects.all()


class WorkersListView(generics.ListCreateAPIView):
    model = Worker
    serializer_class = WorkerSerializer

    def get_queryset(self):
        return Worker.objects.all()


class AllItemsListView(generics.ListCreateAPIView):
    model = Item
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.all()


class UnborrowedItemsListView(generics.ListCreateAPIView):
    model = Item
    serializer_class = ItemSerializer

    def get_queryset(self):
        items = Item.objects.all()
        borrowed_pks = []
        for item in items:
            if BorrowedItem.objects.filter(item=item).count():
                borrowed_pks.append(item.pk)
        items = Item.objects.exclude(pk__in=borrowed_pks)
        return items


class BorrowedItemDetailView(APIView):

    def get(self, request, pk, *args, **kwargs):
        borrowed_item = BorrowedItem.objects.get(pk=pk)
        serializer = BorrowedItemSerializer(borrowed_item)
        return Response(serializer.data)


class WorkerDetailView(APIView):

    def get(self, request, pk, *args, **kwargs):
        worker = Worker.objects.get(pk=pk)
        serializer = WorkerSerializer(worker)
        return Response(serializer.data)



class ItemDetailView(APIView):

    def get(self, request, pk, *args, **kwargs):
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
