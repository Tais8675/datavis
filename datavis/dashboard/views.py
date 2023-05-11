from django.shortcuts import render

# Create your views here.

dt =[
          7000,
          21345,
          18483,
          24003,
          23489,
          24092,
          26034
  ]

def index(request):
    return render(request, 'index.html', {"dt2": dt})
