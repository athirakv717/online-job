from django.shortcuts import render
from service_request.models import ServiceRequest
import datetime

# Create your views here.
def post_srvc_reqst(request):
    if request.method == "POST":
        ob = ServiceRequest()
        ob.service_request = request.POST.get('service_request')
        ob.action=request.POST.get('actions')
        ob.date=datetime.datetime.today()

    return render(request,'service_request/post service rqst.html')

def srvc_reqst_actns(request):
    if request.method == "POST":
        ob = ServiceRequest()
        ob.action = request.POST.get('actions')
    return render(request, 'service_request/service request actions.html')

def view_srvc_reqst(request):
    ob = ServiceRequest.objects.all()
    context = {
        'ok': ob
    }
    return render(request, 'service_request/view service requestss.html', context)