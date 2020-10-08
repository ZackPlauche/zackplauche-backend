# Generated by Django 3.1.2 on 2020-10-08 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20201008_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address_1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='phone Number (Cell)'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
