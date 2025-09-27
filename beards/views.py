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
		order_id = request.GET.get("order_id")
		if order_id:
			order = Order.objects.filter(id=order_id).first()
			order = OrderSerializer(order).data
			return Response(order)

		orders = Order.objects.all()
		orders = OrderSerializer(orders, many=True).data
		# Order.objects.all().delete()
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
			user=request.user,
			order=order,
			username=username,
			phone=phone
			# total_price=total_price
		)
		order = OrderSerializer(order).data
		return Response(order)

	def put(self, request):
		order_id = request.data.get("order_id")
		status = request.data.get("status")
		print(request.data)
		if not all([order_id, status]):
			return Response({"status": False, "message": "order_id and status are required"})

		order = Order.objects.filter(id=order_id).first()
		if not order:
			return Response({"status": False, "message": "Order not found"})
		order.status = status
		order.save()
		order = OrderSerializer(order).data
		return Response(order)


