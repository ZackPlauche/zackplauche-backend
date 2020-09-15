# Generated by Django 3.0.5 on 2020-09-10 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20200909_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='deliverables',
            field=models.ManyToManyField(blank=True, to='services.Deliverable'),
        ),
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
