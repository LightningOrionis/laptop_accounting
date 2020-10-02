from datetime import datetime

from django.test import TestCase, Client

from .models import *

class HttpResponseTest(TestCase):

    def setUp(self):
        self.c = Client()
        w = Worker.objects.create(name='test_worker', team='testers')
        i = Item.objects.create(title='item', type='NB', price=200,
                                configuration_link='https://hello.world')
        borrowed_item = BorrowedItem.objects.create(item=i, borrower=w,
                                                    paid_by='abc', comment='aa')


    def test_connection_index(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_connection_borrowed_list(self):
        response = self.c.get('/borrowed_list')
        self.assertEqual(response.status_code, 200)

    def test_connection_workers_list(self):
        response = self.c.get('/workers_list')
        self.assertEqual(response.status_code, 200)

    def test_connection_items_list(self):
        response = self.c.get('/items_list')
        self.assertEqual(response.status_code, 200)

    def test_connection_create_worker(self):
        response = self.c.get('/new_worker')
        self.assertEqual(response.status_code, 200)

    def test_coonection_update_worker(self):
        response = self.c.get('/worker/1/update')
        self.assertEqual(response.status_code, 200)

    def test_connection_delete_worker(self):
        response = self.c.get('/worker/1/delete')
        self.assertEqual(response.status_code, 200)

    def test_connection_worker_detail_8(self):
        response = self.c.get('/worker/1')
        self.assertEqual(response.status_code, 200)

    def test_connection_create_item(self):
        response = self.c.get('/new_item')
        self.assertEqual(response.status_code, 200)

    def test_connection_update_item(self):
        response = self.c.get('/item/1/update')
        self.assertEqual(response.status_code, 200)

    def test_connection_delete_item(self):
        response = self.c.get('/item/1/delete')
        self.assertEqual(response.status_code, 200)

    def test_connection_borrow_item(self):
        response = self.c.get('/item/1/borrow')
        self.assertEqual(response.status_code, 200)
