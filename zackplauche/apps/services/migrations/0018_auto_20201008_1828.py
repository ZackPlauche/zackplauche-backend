# Generated by Django 3.1.2 on 2020-10-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_auto_20200915_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(editable=False, max_length=255, unique=True),
        ),
    ]