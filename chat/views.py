from email import message
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, DeleteView, View, ListView
from .models import Room, Message
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from urllib import request
import secrets
from rest_framework import viewsets
from .serializers import UserSerializer, MessageSerializer

def group(request):
	context = {
		'chatid': secrets.token_hex(10)
		}
	return render(request, 'group.html', context)

class RoomView(View):
	def get(self, request, pk, *args, **kwargs):
		username = request.GET.get('username')
		room = Room.objects.get(pk=pk)
		if room.allowed_users.filter(id=request.user.id).exists():
			message_value=[]
			message_list = Message.objects.filter(room=pk)
			for message in message_list:
				message_value.append(str(message.value))
			zipped_message_list = zip(message_list, message_value)
			context = {
				'username': username,
				'room': room.name,
				'creator_id':room.creator.id,
				'creator_name':room.creator,
				'users_count': room.allowed_users.count(),
				'zipped_message_list': zipped_message_list,
			}
			return render(request, 'room.html', context)
		else:
			return redirect('group')

def checkview(request):
	room = request.POST['room_name']
	if Room.objects.filter(name=room, allowed_users=request.user).exists():
		room = Room.objects.filter(name=room)[0]
		return redirect('room', pk=room.pk, room=room.name)
	else:
		new_room = Room.objects.create(name=room, creator=request.user)
		new_room.allowed_users.add(request.user)
		new_room.save()
		room = Room.objects.filter(name=room)[0]
		return redirect('room', pk=room.pk, room=room.name)

class SendGroupMessage(View):
	def post(self, request, pk, *args, **kwargs):
		room = Room.objects.get(pk=pk)
		message = request.POST.get('message'),
		if message[0] == None:
			return redirect('room', pk=pk, room=room.name)
		new_message = Message(
				value=message[0],
				user=request.user,
				room=room,
				)
		new_message.save()
		return redirect('room', pk=pk, room=room.name)


class AddAllowedUserView(View):
	def post(self, request, pk, *args, **kwargs):
		room = Room.objects.get(pk=pk)
		allowed_user=request.POST.get('alloweduser')
		uid = User.objects.get(username=allowed_user).id
		if room.creator.id == request.user.id:
			if room.allowed_users.filter(id=uid).exists():
				room.allowed_users.remove(uid)
			else:
				room.allowed_users.add(uid)

			return redirect('room', pk=pk, room=room.name)
		else:
			return redirect('room', pk=pk, room=room.name)

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class MessageViewSet(viewsets.ModelViewSet):
	queryset = Message.objects.all()
	serializer_class = MessageSerializer
