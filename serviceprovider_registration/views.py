from django.http import HttpResponseRedirect
from django.shortcuts import render
from service_provider.models import SrRegistration
from login.models import  Login
# from http import HttpResponseRedirect

# Create your views here.

def add_srvc_prvdr(request):
    if request.method == "POST":
      ob = SrRegistration()
      ob.name = request.POST.get('name')
      ob.service = request.POST.get('service')
      ob.location = request.POST.get('location')
      ob.contact = request.POST.get('contact')
      ob.email = request.POST.get('email')
      ob.username = request.POST.get('user')
      ob.password = request.POST.get('pass')
      # ob.action = request.POST.get('')
      ob.dob = request.POST.get('age')
      ob.phone = request.POST.get('Phone')
      ob.save()

      # obj=Login()
      # obj.username= ob.username
      # obj.password= ob.password
      # obj.type='service_provider'
      # obj.uid= ob.sid
      # obj.save()
    return render(request, 'service_provider/add service provider(admin).html')



def srvc_prvdr_prfle(request,idd):
    ob = SrRegistration.objects.get(spid=idd)
    context = {
        'okk': ob
    }
    if request.method == "POST":
        ob = SrRegistration.objects.get(spid=idd)
        ob.name = request.POST.get('name')
        ob.age = request.POST.get('age')
        ob.address = request.POST.get('address')
        ob.phone = request.POST.get('phone')
        ob.email = request.POST.get('email')
        ob.gender = request.POST.get('gender')
        ob.service = request.POST.get('service')
        ob.location = request.POST.get('location')
        ob.contact = request.POST.get('contact')
        ob.save()
        return render(request, 'service_provider/sr_editprofile.html')
    return render(request, 'service_provider/service provider profile.html',context)





def ser(request):
    ss=request.session["uid"]
    ob = SrRegistration.objects.filter(spid=ss)
    print(ss)
    context = {
        'll': ob
    }
    print(len(ob))
    return render(request, 'service_provider/servicecopy.html',context)


def view_srvc_prvdr(request):
    ob = SrRegistration.objects.all()
    context = {
        'okk': ob
    }
    return render(request, 'service_provider/view serviceprvdr(admin).html', context)

def sr_editprofile(request,idd):
    ob = SrRegistration.objects.get(spid=idd)
    context = {
        'okk': ob
    }
    if request.method == "POST":
       ob = SrRegistration.objects.get(spid=idd)
       ob.name = request.POST.get('name')
       ob.address = request.POST.get('location')
       ob.service = request.POST.get('service')
       ob.dob = request.POST.get('age')
       ob.email = request.POST.get('email')
       ob.phone = request.POST.get('contact')
       ob.save()
       return HttpResponseRedirect('/service_provider/serv')
    return render(request, 'service_provider/sr_editprofile.html',context)

def sr_profile(request):
        ob = SrRegistration.objects.all()
        context = {
            'ok': ob
        }
        return render(request, 'service_provider/view_srprofile.html', context)

def sr_list(request,idd):
       ob = SrRegistration.objects.get(spid=idd)
       context = {
           'ok': ob
       }
       if request.method=="POST":
           ob= SrRegistration.objects.get(spid=idd)
           ob.ob.name = request.POST.get('name')
           ob.service = request.POST.get('service')
           ob.location = request.POST.get('location')
       return render(request,'service_provider/sr_list.html',context)