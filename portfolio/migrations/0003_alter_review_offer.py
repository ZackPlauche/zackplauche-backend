# Generated by Django 4.0.1 on 2022-11-07 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_review_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='portfolio.offer'),
        ),
    ]
