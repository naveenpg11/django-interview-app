# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from chat.models import Room , Message, Status
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
	getRooms=Room.objects.all()
	return render(request, 'home.html', {'Room': getRooms})

def chatroom(request ,labels):
	room=Room.objects.get(label=labels)
	#Get the recent 5 messages from the Messages Table ! 
	msg = reversed(room.messages.order_by('-timestamp')[:5])
	#msg=Message.objects.filter(room=room).order_by('-timestamp')[:5]
	status=Status.objects.filter(room=labels)
	return render(request, 'chat.html', {'rooom':room, 'messages':msg ,'Online':status})
	


