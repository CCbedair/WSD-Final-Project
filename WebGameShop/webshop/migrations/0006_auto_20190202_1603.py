# Generated by Django 2.1.3 on 2019-02-02 16:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webshop', '0005_auto_20190202_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='developer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='game',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='game',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='game',
            name='title',
        ),
        migrations.AddField(
            model_name='game',
            name='icon',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(default='UNKNOWN', max_length=200),
        ),
        migrations.AddField(
            model_name='game',
            name='price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='player',
            name='games',
            field=models.ManyToManyField(blank=True, to='webshop.Game'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='game',
            name='tags',
            field=models.ManyToManyField(to='webshop.Tag'),
        ),
    ]
