# Generated by Django 3.0.5 on 2020-06-02 11:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models
import uuid


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
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('short_description', models.TextField(help_text='Max characters: 500', max_length=500, null=True)),
                ('long_description', tinymce.models.HTMLField(blank=True, help_text='Optional long description for service page.', null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('call_to_action', models.CharField(choices=[('Sell', (('Order Now', 'Order Now'), ('Hire Zack', 'Hire Zack'), ('Hire My Team', 'Hire My Team'), ('Book a Call', 'Book a Call'), ('Get Training', 'Get Training'))), ('Contact', (('Contact Us', 'Contact Us'), ('Get Help Now', 'Get Help Now'), ('Get in Touch', 'Get in Touch')))], default='Order Now', max_length=30)),
                ('display', models.BooleanField(default=True)),
                ('deliverables', models.ManyToManyField(to='services.Deliverable')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.Service')),
            ],
        ),
    ]
