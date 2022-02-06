# Generated by Django 4.0.1 on 2022-01-19 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('file', models.FileField(blank=True, null=True, upload_to='downloads/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(max_length=255, verbose_name='alt / title')),
                ('file', models.ImageField(blank=True, null=True, upload_to='icons/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(max_length=255, verbose_name='alt / title')),
                ('file', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('author_name', models.CharField(blank=True, max_length=255)),
                ('author_image', models.ImageField(upload_to='')),
                ('active', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('icon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.icon')),
            ],
            options={
                'verbose_name_plural': 'technologies',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.TextField(blank=True)),
                ('long_description', models.TextField(blank=True)),
                ('site_url', models.URLField(blank=True)),
                ('github_url', models.URLField(blank=True)),
                ('video_url', models.URLField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=True)),
                ('technologies', models.ManyToManyField(help_text='Technologies used for this project.', to='portfolio.Technology')),
                ('thumbnail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.image')),
            ],
        ),
    ]