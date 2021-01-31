# Generated by Django 3.1.2 on 2021-01-05 15:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0021_company_worked_with'),
        ('blog', '0002_post_related_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='https://via.placeholder.com/1800x1200', upload_to='images/')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('body', tinymce.models.HTMLField(default='')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='blog.author')),
                ('related_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.service')),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.article'),
        ),
    ]