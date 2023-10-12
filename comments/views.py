from django.shortcuts import render
from comments.models import Comments
import datetime
# Create your views here.
def comnt(request):
    if request.method == "POST":
        ob = Comments()
        ob.comment = request.POST.get('com')
        ob.service_provider = request.POST.get('sp')
        ob.location = request.POST.get('loc')
        ob.date=datetime.datetime.today()

        ob.save()
    return render(request, 'comments/post comments.html')


def view_cmmnts(request):
    ob = Comments.objects.all()
    context = {
        'ok': ob
    }
    return render(request, 'comments/view comments(service provider).html', context)


