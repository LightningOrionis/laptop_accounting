# Generated by Django 3.1.2 on 2020-10-02 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201002_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='image',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
