from django.shortcuts import render
# from customer.models import
from login.models import Login
from registration.models import Registration


# Create your views here.
def user_reg(request):

    if request.method == "POST":
        ob = Registration()
        ob.fname = request.POST.get('firstname')
        ob.lname = request.POST.get('lastname')
        ob.email = request.POST.get('email')
        ob.phone = request.POST.get('Phone')
        ob.address = request.POST.get('address')
        ob.age = request.POST.get('dob')
        ob.password = request.POST.get('pass')
        ob.save()

        obj=Login()
        obj.username=ob.fname
        obj.password=ob.password
        obj.type='customer'
        obj.uid=ob.rid
        obj.save()
    return render(request, 'registration/registration form.html')