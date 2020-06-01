from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Requirement(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class Technology(models.Model):
    icon = models.ImageField(upload_to="images/", null=True)
    name = models.CharField(max_length=20, null=True)
    url = models.URLField("URL", null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Contributor(models.Model):
    profile_picture = models.ImageField(upload_to="images/", null=True, blank=True, help_text="1:1 Ratio (Square image) for best results.")
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True, help_text="If you're uncomfortable having your last name displayed, simply put your last initial followed by a period.")

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()

class Project(models.Model):
    image = models.ImageField(upload_to="images/", null=True, help_text="Image must be 3:2 ratio, otherwise it'll look distored.")
    title = models.CharField(max_length=100, unique=True, null=True, help_text="Maximum 100 characters.")
    subtitle = models.CharField(max_length=50, null=True, blank=True, help_text="Text that will be shown on the index page for your projects.")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    purpose = models.CharField(max_length=200, null=True, blank=True, help_text="Why are you creating the project? Max Characters: 200")
    description = HTMLField(null=True, blank=True, help_text="Descibe your project in more detail.")
    how_it_works = HTMLField(null=True, blank=True, help_text="Describe how your project works.")
    technologies_used = models.ManyToManyField(Technology, blank=True, help_text="Which techonologies did you use to create this project?")
    contributors = models.ManyToManyField(Contributor, blank=True, help_text="Who helped you on this project?")
    future_plans = HTMLField(null=True, blank=True, help_text="State any plans you might have for this app in the future (this is the closing text section.)")
    requirements = models.ManyToManyField(Requirement, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    github_repository = models.URLField(null=True, blank=True, help_text="Link to your project's github repository (if applicable).")
    demo_vid_url = models.URLField("Demo video embed URL", null=True, blank=True, help_text="Add a link to a video walking through your project.")
    live_url = models.URLField("Live URL", null=True, blank=True, help_text="Link to where your app is hosted (if applicable).")
    download_file = models.FileField(upload_to="software/", null=True, blank=True)
    STATUS_CHIOCES = (
        ('Idea', 'Idea'),
        ('Planning', 'Planning'),
        ('Designing', 'Designing'),
        ('Building', 'Building'),
        ('Almost Done', 'Almost Done'),
        ('Completed', 'Completed')
    )
    status = models.CharField(default="Idea", max_length=50, choices=STATUS_CHIOCES)

    display = models.BooleanField(default=False, help_text="Check if you want this project to be displayed on your site.")
    favorite = models.BooleanField(default=False)
    order = models.PositiveIntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['order', 'display', 'title']


    @property
    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title
