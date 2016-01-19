from django.shortcuts import render
from django.utils import timezone

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect

from django.views import generic
# note generic.DetailView expects the primary key value captured from the URL to be called "pk"
from .forms import SiteLogForm
from .models import SiteLog, Sample

class IndexView(generic.ListView):
    template_name = 'sitelog/index.html'
    context_object_name = 'latest_log_list'

    def get_queryset(self):
        """Return the last five sitelogs."""
        return SiteLog.objects.order_by('-visit_date')[:5]

def new_log(request):
    if request.method == "POST":
        form = SiteLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.author = request.user
            log.save()
            return redirect('list')

    else:
        form = SiteLogForm()

    return render(request, 'sitelog/new.html', {'form': form})


class DetailView(generic.DetailView):
    model = SiteLog
    template_name = 'sitelog/detail.html'

def log_list(request):
    logs = SiteLog.objects.filter(visit_date__lte=timezone.now()).order_by('visit_date')
    return render(request, 'sitelog/list.html', {'logs': logs})



