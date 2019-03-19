# Generated by Django 2.1.3 on 2019-02-02 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0006_auto_20190202_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unque_payment_id', models.CharField(max_length=2000, unique=True)),
                ('amount', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('beneficiary', models.CharField(max_length=2000)),
                ('recipient', models.CharField(max_length=2000)),
                ('state', models.CharField(choices=[('rejected', 'rejected'), ('in progress', 'in progress'), ('completed', 'completed')], default='in progress', max_length=1)),
            ],
        ),
    ]