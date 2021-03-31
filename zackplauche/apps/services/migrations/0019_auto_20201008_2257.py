# Generated by Django 3.1.2 on 2020-10-08 19:57

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_auto_20201008_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='created_date',
        ),
        migrations.RemoveField(
            model_name='client',
            name='address_one',
        ),
        migrations.RemoveField(
            model_name='client',
            name='address_two',
        ),
        migrations.RemoveField(
            model_name='client',
            name='company_logo',
        ),
        migrations.RemoveField(
            model_name='client',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='company_website',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='client_name',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order',
            name='price_total',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.CharField(choices=[('primary', 'Primrary'), ('standard', 'Standard'), ('microservice', 'Microservice')], default='standard', max_length=50, verbose_name='type'),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, upload_to='company_logos/')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('website', models.URLField(blank=True)),
                ('legal_stucture', models.CharField(choices=[('sole proprietor', 'Sp'), ('partnership', 'Ps'), ('limited liability company', 'Llc'), ('corporation', 'Corp'), ('s corporation', 'S Corp')], max_length=255)),
                ('is_sponsor', models.BooleanField(default=False)),
                ('clients', models.ManyToManyField(related_name='companies', to='services.Client')),
                ('parent_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.company')),
            ],
        ),
    ]