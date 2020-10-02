from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from .models import *


def index(request):
    return render(request, 'index.html')


# as class
def borrowed_list(request):
    borrowed_items = BorrowedItem.objects.all()
    number_iterator = range(1, borrowed_items.count() + 1)
    borrowed_items_iterator = zip(number_iterator, borrowed_items)
    context = {'borrowed_items': borrowed_items_iterator }
    return render(request, 'borrowed_list.html', context)


# as class
def workers_list(request):
    workers_list = Worker.objects.all()
    context = {'workers_list': workers_list}
    return render(request, 'workers_list.html', context)


# as class
def items_list(request):
    items = Item.objects.all()
    number_iterator = range(1, items.count() + 1)
    items_iterator = zip(number_iterator, items)
    context = {'items_list': items_iterator}
    return render(request, 'items_list.html', context)


class CreateWorker(CreateView):
    model = Worker
    template_name = 'create_worker.html'
    fields = ['name', 'team']

    def get_success_url(self):
        return reverse('workers_list')


class UpdateWorker(UpdateView):
    model = Worker
    template_name = 'update_worker.html'
    fields= ['name', 'team']

    def get_success_url(self):
        return reverse('workers_list')


class DeleteWorker(DeleteView):
    model = Worker
    template_name = 'worker_confirm_delete.html'

    def get_success_url(self):
        return reverse('workers_list')
