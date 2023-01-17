from django.shortcuts import render
from . import models

def cv(request):
    lan = models.language.objects.all
    skill = models.skills.objects.all
    expert = models.expertise.objects.all
    edu = models.education.objects.all
    return render(request, 'cv.html', {'lan':lan,'skill':skill,'expert':expert,'edu':edu})
