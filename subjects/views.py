from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def index(req: HttpRequest):
  return render(req, "index.html")

def subject(req, value):
  print(value)
  return render(req, "index.html")