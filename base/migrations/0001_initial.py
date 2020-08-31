# Generated by Django 3.0.5 on 2020-08-31 10:06

import django.core.validators
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('logo', models.ImageField(null=True, upload_to='images')),
                ('website', models.URLField(blank=True, null=True)),
                ('display', models.BooleanField(default=True)),
                ('order', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['display', 'order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('progress', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('color', models.CharField(choices=[('Blue', 'Blue'), ('Green', 'Green'), ('Grey', 'Grey'), ('Red', 'Red'), ('White', 'White'), ('Yellow', 'Yellow')], default='White', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
    ]
