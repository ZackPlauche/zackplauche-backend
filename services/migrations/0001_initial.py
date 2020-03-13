# Generated by Django 3.0 on 2020-03-11 13:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('short_description', models.TextField(help_text='Max characters: 500', max_length=500, null=True)),
                ('long_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('call_to_action', models.CharField(choices=[('Sell', (('Order Now', 'Order Now'), ('Hire Zack', 'Hire Zack'), ('Hire My Team', 'Hire My Team'), ('Book a Call', 'Book a Call'), ('Get Training', 'Get Training'))), ('Contact', (('Contact Us', 'Contact Us'), ('Get Help Now', 'Get Help Now'), ('Get in Touch', 'Get in Touch')))], default='Order Now', max_length=30)),
                ('display', models.BooleanField(blank=True, default=True, null=True)),
                ('deliverables', models.ManyToManyField(to='services.Deliverable')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('service_ordered', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
            ],
        ),
    ]
