# Generated by Django 2.1.3 on 2018-11-15 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0002_auto_20181115_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='', unique=True),
        ),
    ]
