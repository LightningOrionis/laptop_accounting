from datetime import datetime

from django.test import TestCase, Client

from .models import *

class HttpResponseTest(TestCase):

    def setUp(self):
        self.c = Client()
        Worker.objects.create(name='test_worker', team='testers',
                              image='logo.png')
        Item.objects.create(title='item', type='NB', price=200,
                            configuration_link='https://hello.world')

    def test_connection_index_200(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_connection_borrowed_list_200(self):
        response = self.c.get('/borrowed_list')
        self.assertEqual(response.status_code, 200)

    def test_connection_workers_list_200(self):
        response = self.c.get('/workers_list')
        self.assertEqual(response.status_code, 200)

    def test_connection_items_list_200(self):
        response = self.c.get('/items_list')
        self.assertEqual(response.status_code, 200)

    def test_connection_create_worker_200(self):
        response = self.c.get('/new_worker')
        self.assertEqual(response.status_code, 200)

    def test_coonection_update_worker_200(self):
        worker = Worker.objects.get(name='test_worker')
        response = self.c.get('/worker/{0}/update'.format(worker.pk))
        self.assertEqual(response.status_code, 200)

    def test_coonection_update_worker_404(self):
        response = self.c.get('/worker/228/update')
        self.assertEqual(response.status_code, 404)

    def test_connection_delete_worker_200(self):
        worker = Worker.objects.get(name='test_worker')
        response = self.c.get('/worker/{0}/delete'.format(worker.pk))
        self.assertEqual(response.status_code, 200)

    def test_coonection_delete_worker_404(self):
        response = self.c.get('/worker/228/delete')
        self.assertEqual(response.status_code, 404)

    def test_connection_worker_detail_200(self):
        worker = Worker.objects.get(name='test_worker')
        response = self.c.get('/worker/{0}'.format(worker.pk))
        self.assertEqual(response.status_code, 200)

    def test_coonection_worker_detail_302(self):
        response = self.c.get('/worker/228')
        self.assertEqual(response.status_code, 302)

    def test_connection_create_item_200(self):
        response = self.c.get('/new_item')
        self.assertEqual(response.status_code, 200)

    def test_connection_update_item_200(self):
        item = Item.objects.get(title='item')
        response = self.c.get('/item/{0}/update'.format(item.pk))
        self.assertEqual(response.status_code, 200)

    def test_connection_update_item_404(self):
        response = self.c.get('/item/1337/update')
        self.assertEqual(response.status_code, 404)

    def test_connection_delete_item_200(self):
        item = Item.objects.get(title='item')
        response = self.c.get('/item/{0}/delete'.format(item.pk))
        self.assertEqual(response.status_code, 200)

    def test_connection_delete_item_404(self):
        response = self.c.get('/item/1337/delete')
        self.assertEqual(response.status_code, 404)

    def test_connection_borrow_item_200(self):
        response = self.c.get('/item/1/borrow')
        self.assertEqual(response.status_code, 200)

    def test_connection_return_item_200(self):
        item = Item.objects.get(title='item')
        borrower = Worker.objects.get(name='test_worker')
        borrowed_item = BorrowedItem.objects.create(item=item, borrower=borrower,
                                                    paid_by='abc', comment='ab')
        response = self.c.get('/borrowed_item/{0}/return'.format(borrowed_item.pk))
        self.assertEqual(response.status_code, 302)


class ModelTest(TestCase):

    def setUp(self):
        self.item = Item.objects.create(title='abc', configuration_link='https://hi.ru',
                                        price='1450', type='NB')
        self.borrower = Worker.objects.create(name='worker', team='abc',
                                              image = 'img')
        self.borrowed_item = BorrowedItem.objects.create(item=self.item,
                                                         borrower=self.borrower,
                                                         paid_by='smb',
                                                         comment='123')

    def test_str_item(self):
        self.assertEqual(str(self.item), 'abc')

    def test_str_borrowed_item(self):
        self.assertEqual(str(self.borrowed_item), 'abc')

    def test_str_worker(self):
        self.assertEqual(str(self.borrower), 'worker')
