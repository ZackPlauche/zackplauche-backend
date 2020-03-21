# Generated by Django 3.0 on 2020-03-20 06:40

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, help_text='1:1 Ratio for best results.', null=True, upload_to='images/')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(help_text="If you're uncomfortable having your last name displayed, simply put your last initial followed by a period.", max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(null=True, upload_to='images/')),
                ('name', models.CharField(max_length=20, null=True)),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text="Image must be 3:2 ratio, otherwise it'll look distored.", null=True, upload_to='images/')),
                ('title', models.CharField(help_text='Maximum 100 characters.', max_length=100, null=True, unique=True)),
                ('subtitle', models.CharField(blank=True, help_text='Text that will be shown on the index page for your projects.', max_length=30, null=True)),
                ('purpose', models.CharField(blank=True, help_text='Why are you creating the project? Max Characters: 200', max_length=200, null=True)),
                ('description', tinymce.models.HTMLField(blank=True, help_text='Descibe your project in more detail.', null=True)),
                ('how_it_works', tinymce.models.HTMLField(blank=True, help_text='Describe how your project works.', null=True)),
                ('future_plans', tinymce.models.HTMLField(blank=True, help_text='State any plans you might have for this app in the future (this is the closing text section.)', null=True)),
                ('github_repository', models.URLField(blank=True, help_text="Link to your project's github repository (if applicable).", null=True)),
                ('demo_vid_url', models.URLField(blank=True, help_text='Add a link to a video walking through your project.', null=True, verbose_name='Demo video embed URL')),
                ('live_url', models.URLField(blank=True, help_text='Link to where your app is hosted (if applicable).', null=True, verbose_name='Live URL')),
                ('download_file', models.FileField(blank=True, null=True, upload_to='software/')),
                ('status', models.CharField(choices=[('Idea', 'Idea'), ('Planning', 'Planning'), ('Designing', 'Designing'), ('Building', 'Building'), ('Almost Done', 'Almost Done'), ('Completed', 'Completed')], default='Idea', max_length=50)),
                ('display', models.BooleanField(default=False, help_text='Check if you want this project to be displayed on your site.')),
                ('favorite', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Category')),
                ('contributors', models.ManyToManyField(blank=True, help_text='Who helped you on this project?', to='portfolio.Contributor')),
                ('requirements', models.ManyToManyField(blank=True, to='portfolio.Requirement')),
                ('tag', models.ManyToManyField(blank=True, to='portfolio.Tag')),
                ('technologies_used', models.ManyToManyField(blank=True, help_text='Which techonologies did you use to create this project?', to='portfolio.Technology')),
            ],
        ),
    ]
