from django.shortcuts import render
from .models import dados

# Create your views here.

# dt =[
#           7000,
#           21345,
#           18483,
#           24003,
#           23489,
#           24092,
#           26034
#   ]

def index(request):
    dt = []
    values = dados.objects.all()
    for v in values:
        dt.append(v.value)
    return render(request, 'index.html', {"dt2": dt})


# def index(request):
#     return render(request, 'index.html', {"dt2": dt})
