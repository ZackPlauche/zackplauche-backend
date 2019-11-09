Features of this app:
1. I added {{ string|linebreaksbr }} functionality to linebreak text directly from model
2. I added GIFs to site
3. I used Django templating language (including "block") to create templates on the site.
4. I learned how to call images to the site via {{ model.image.url }} and + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
5. I learned how to call css & static files WITH model images using static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) url urlpatterns
6. I created dynamic slug url dispatchers using slugify & @property, with custom for loop filter in the settings for blog and services
7. I directed my images to MEDIA_URL and MEDIA_ROOT
8. I built custom models to help me on my path here.
9. Properly specified url, static, and templates directories (for url, this includes adding "app_name = 'app'" to the urls.py file)
10. Using a core app for core site functionality (app is named "home", but could be called "core" or "base" etc.)
11. Added built in for block level static importing: ('builtins': ['django.contrib.staticfiles.templatetags.staticfiles', inside of templates setting))
12. Use of Django template {% lorem %} tag to generate lorem ipsum text.
13.
