from django.shortcuts import render

from .forms import SiteLogForm

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def new_log(request):
    form = SiteLogForm
    return render(request, 'sitelog/new.html', {'form': form})

