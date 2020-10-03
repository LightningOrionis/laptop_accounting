from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from .models import *
from .forms import BorrowItemForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class BorrowedItemsListView(View):
    def get(self, request, *args, **kwargs):
        borrowed_items = BorrowedItem.objects.all()
        if not borrowed_items.count():
            borrowed_items_iterator = None
        else:
            number_iterator = range(1, borrowed_items.count() + 1)
            borrowed_items_iterator = zip(number_iterator, borrowed_items)
        context = {'borrowed_items': borrowed_items_iterator }
        return render(request, 'borrowed_list.html', context)


class WorkersListView(View):
    def get(self, request, *args, **kwargs):
        workers_list = Worker.objects.all()
        context = {'workers_list': workers_list}
        return render(request, 'workers_list.html', context)


class ItemsListView(View):
    def get(self, request, *args, **kwargs):
        items = Item.objects.all()
        borrowed_pks = []
        for item in items:
            if BorrowedItem.objects.filter(item=item).count():
                borrowed_pks.append(item.pk)
        items = Item.objects.exclude(pk__in=borrowed_pks)
        if not items.count():
            items_iterator = None
        else:
            number_iterator = range(1, items.count() + 1)
            items_iterator = zip(number_iterator, items)
        context = {'items_list': items_iterator}
        return render(request, 'items_list.html', context)


class CreateWorkerView(CreateView):
    model = Worker
    template_name = 'create_worker.html'
    fields = ['name', 'team', 'image']

    def get_success_url(self):
        return reverse('workers_list')


class UpdateWorkerView(UpdateView):
    model = Worker
    template_name = 'update_worker.html'
    fields= ['name', 'team', 'image']

    def get_success_url(self):
        return reverse('workers_list')


class DeleteWorkerView(DeleteView):
    model = Worker
    template_name = 'worker_confirm_delete.html'

    def get_success_url(self):
        return reverse('workers_list')


class CreateItemView(CreateView):
    model = Item
    template_name = 'create_item.html'
    fields = ['title', 'configuration_link', 'price', 'type']

    def get_success_url(self):
        return reverse('items_list')


class UpdateItemView(UpdateView):
    model = Item
    template_name = 'update_item.html'
    fields = ['title', 'configuration_link', 'price', 'type']

    def get_success_url(self):
        return reverse('items_list')


class DeleteItemView(DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'

    def get_success_url(self):
        return reverse('items_list')


class BorrowItemView(View):
    form_class = BorrowItemForm
    template_name = 'borrow_item.html'

    def get(self, request, id, *args, **kwargs):
        if id != "new":
            try:
                item = Item.objects.get(id=int(id))
                initial = {'item': item}
            except:
                initial = {}
        else:
            initial = {}
        form = self.form_class(initial=initial)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            borrowed_item = form.save(commit=False)
            borrowed_item.save()
            return HttpResponseRedirect(reverse('borrowed_list'))
        context = {'form': form}
        return render(request, self.template_name, context)


class ReturnItemView(DeleteView):
    model = BorrowedItem

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse('borrowed_list')


class WorkerDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            worker = Worker.objects.get(pk=pk)
        except:
            return redirect('/workers_list')
        borrowed_items = BorrowedItem.objects.filter(borrower=worker)
        if not borrowed_items.count():
            items_iterator = None
        else:
            number_iterator = range(1, borrowed_items.count() + 1)
            items_iterator = zip(number_iterator, borrowed_items)
        context = {'worker': worker, 'borrowed_items': items_iterator}
        return render(request, 'worker_detail.html', context)
