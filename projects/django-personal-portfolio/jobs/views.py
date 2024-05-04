from django.shortcuts import render, get_object_or_404
from .models import Job
# Create your views here.


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})


def job_detail(request, job_id):
    # job = Job.objects.get(id=job_id)
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})
