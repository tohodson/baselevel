from django.shortcuts import render
from django.utils import timezone

from django.http import HttpResponse

from .forms import SiteLogForm
from .models import SiteLog

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def new_log(request):
    form = SiteLogForm()
    return render(request, 'sitelog/new.html', {'form': form})

def log_list(request):
    logs = SiteLog.objects.filter(visit_date__lte=timezone.now()).order_by('visit_date')
    return render(request, 'sitelog/list.html', {'logs': logs})



