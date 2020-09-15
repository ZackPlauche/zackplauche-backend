# Generated by Django 3.0.5 on 2020-09-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200910_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('webapp', 'Webapp'), ('ecommerce_store', 'Ecommerce Store')], default='webapp', max_length=150, verbose_name='type'),
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
