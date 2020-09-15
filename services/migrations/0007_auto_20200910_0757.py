# Generated by Django 3.0.5 on 2020-09-10 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_service_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='payment_type',
            field=models.CharField(choices=[('in full', 'In Full'), ('split payments', 'Split Payments'), ('hourly', 'Hourly')], default='in full', max_length=50),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.CharField(choices=[('service', 'Service'), ('microservice', 'Microservice')], default='service', max_length=50, verbose_name='type'),
        ),
    ]
