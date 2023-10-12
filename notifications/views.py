from django.shortcuts import render
from notifications.models import Notifications
import datetime

# Create your views here.
def ntfcts(request):
    if request.method == "POST":
        ob = Notifications()
        ob.notification = request.POST.get('post notifications')
        ob.date=datetime.datetime.today()
        ob.save()
    return render(request, 'notifications/post notifications.html')

def view_ntfctns(request):
    ob = Notifications.objects.all()
    context ={
        'ok':ob
    }
    return render(request, 'notifications/view notifications.html', context)


def view_srntfs(request):
    ob = Notifications.objects.all()
    context ={
        'ok':ob
    }
    return render(request, 'notifications/view srntfs.html', context)


