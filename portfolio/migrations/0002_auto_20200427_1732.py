# Generated by Django 3.0.5 on 2020-04-27 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order', 'display', 'title']},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='profile_picture',
            field=models.ImageField(blank=True, help_text='1:1 Ratio (Square image) for best results.', null=True, upload_to='images/'),
        ),
    ]
