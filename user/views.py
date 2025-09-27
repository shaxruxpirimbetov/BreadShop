from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework import permissions
from django.shortcuts import render
from .serializers import UserSerializer


class RegisterApi(APIView):
	permission_classes = [permissions.AllowAny]
	def post(self, request):
		username = request.data.get("username")
		password = request.data.get("password")
		if not all([username, password]):
			return Response({"status": False, "message": "username and password are required"})
		
		user = User.objects.filter(username=username).first()
		if user:
			return Response({"status": False, "message": "username already exists"})
		
		user = User.objects.create_user(username=username, password=password)
		user = UserSerializer(user).data
		return Response(user)


class GetMeApi(APIView):
	permission_classes = [permissions.IsAuthenticated]
	def get(self, request):
		return Response(request.user)

