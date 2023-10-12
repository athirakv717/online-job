from django.shortcuts import render
from chat.models import Chat

# Create your views here.
def chat(request):
    if request.method == "POST":
        ob = Chat()
        ob.chat = request.POST.get('chat')

    return render(request, 'chat/chat.html')
