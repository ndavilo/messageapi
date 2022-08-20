from django.contrib.auth.models import User 
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import Message
from chat.serializers import MessageSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import generics

class MessageViewSet(viewsets.ModelViewSet):
	queryset = Message.objects.all()
	serializer_class = MessageSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

@csrf_exempt 
def userList(request, pk=None):
    if request.method == 'GET':
        if pk: 
            users = User.objects.filter(id=pk)
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request}) 
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def messageList(request, sender=None, receiver=None):
    if request.method == 'GET':
        messages = Message.objects.filter(
			sender=User.objects.get(username=sender).id, 
			receiver=User.objects.get(username=receiver).id)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

