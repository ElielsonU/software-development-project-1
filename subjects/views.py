from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.
def index(req: HttpRequest):
  subject = models.Subject.objects.all()
  return render(req, "index.html", { "subjects": subject})

def subject(req, slug):
  subject = models.Subject.objects.filter(slug=slug)
  if (not subject.first()): return HttpResponse("Este curso não existe!")
  return render(req, "subject.html", { "subject": subject.first().__dict__})

def tasklist(request):
  return render(request,'task/list.html')