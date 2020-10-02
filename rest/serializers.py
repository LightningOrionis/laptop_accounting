from rest_framework import serializers

from core.models import *


class BorrowedItemSerializer(serializers.ModelSerializer):
    item = serializers.SlugRelatedField(slug_field='title', read_only=True)
    borrower = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = BorrowedItem
        fields = ('item', 'borrower', 'borrow_date', 'paid_by', 'comment')


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ('name', 'team', 'image')


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('title', 'configuration_link', 'price', 'type')
