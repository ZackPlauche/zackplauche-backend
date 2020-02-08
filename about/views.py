from django.shortcuts import render
from .models import CriteriaForSuccess, Skill, Value

# Create your views here.
def about(request):
    success_criteria = CriteriaForSuccess.objects.all()
    skills = Skill.objects.all().order_by('title')
    values = Value.objects.all()

    context = {
        'success_criteria': success_criteria,
        'skills': skills,
        'values': values,
    }

    return render(request, 'about/about.html', context=context)
