from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework import permissions
from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer


class OrderApi(APIView):
	permission_classes = [permissions.IsAuthenticated]
	def get(self, request):
		orders = Order.objects.all()
		orders = OrderSerializer(orders, many=True).data
		return Response({"status": True, "message": orders})
	
	def post(self, request):
		data = request.data
		order = data.get("order")
		username = data.get("username")
		phone = data.get("phone")
		# total_price = data.get("total_price")
		
		print(data)
		
		if not all([order, username, phone]):
			return Response({"status": False, "message": "order, username, phone and total_price are required"})
		
		order = Order.objects.create(
		    order=order,
		    username=username,
		    phone=phone
		    # total_price=total_price
		)
		order = OrderSerializer(order).data
		return Response(order)
	
	def put(self, request):
		return Response({"status": True})


