from django import forms
from .models import BorrowedItem


class BorrowItemForm(forms.ModelForm):
    class Meta:
        model = BorrowedItem
        fields = ['item', 'borrower', 'paid_by', 'comment']
