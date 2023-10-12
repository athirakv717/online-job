from django.shortcuts import render
from job_notifications.models import JobNotifications
import datetime

# Create your views here.
def jobntfcts(request):
    if request.method == "POST":
        ob = JobNotifications()
        ob.job_notification = request.POST.get('pos')
        ob.date=datetime.datetime.today()
        ob.save()
    return render(request, 'job_notifications/post jobntfctns.html')

def view_ntfctns(request):
    ob = JobNotifications.objects.all()
    context ={
        'ok':ob
    }
    return render(request, 'job_notifications/view jobntfctns.html', context)

def view_srjobntfctns(request):
    ob = JobNotifications.objects.all()
    context ={
        'ok':ob
    }
    return render(request, 'job_notifications/view sr jobntfs.html', context)

