from django.shortcuts import render
from photos.models import Photos

# Create your views here.
def up_photos(request):
    if request.method == "POST":
        ob = Photos()
        ob.photo = request.POST.get('photos')

    return render(request, 'photos/upload_photos.html')

def view_photos(request):
    ob = Photos.objects.all()
    context = {
        'ok': ob
    }
    return render(request, 'photos/view_photos.html', context)