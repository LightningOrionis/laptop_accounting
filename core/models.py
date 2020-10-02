from django.db import models


def get_img_url(worker, filename):
    return 'workers/{0}_{1}'.format(worker.id, filename)


class Item(models.Model):
    TYPE_CHOICES = (
        ('NB', 'Notebook'),
        ('EP', 'Earphones'),
        ('MT', 'Monitor')
    )

    title = models.CharField(max_length=200)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    price = models.IntegerField()
    configuration_link = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Worker(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    image = models.FileField(upload_to=get_img_url)

    def __str__(self):
        return self.name


class BorrowedItem(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Worker, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now=True)
    paid_by = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.item.title
