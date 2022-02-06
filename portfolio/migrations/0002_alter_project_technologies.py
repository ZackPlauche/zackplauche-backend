# Generated by Django 4.0.1 on 2022-02-02 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(blank=True, help_text='Technologies used for this project.', to='portfolio.Technology'),
        ),
    ]
