# Generated by Django 3.0.5 on 2020-09-10 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20200910_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address_one',
            field=models.CharField(default='', max_length=255, verbose_name='address 1'),
        ),
        migrations.AlterField(
            model_name='client',
            name='address_two',
            field=models.CharField(default='', max_length=255, verbose_name='address 2'),
        ),
    ]
