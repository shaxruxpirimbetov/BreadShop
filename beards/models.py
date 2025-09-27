from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	order = models.TextField()
	username = models.TextField()
	phone = models.TextField()
	# total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	status = models.TextField(default="waiting") #Kútilmekte
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f"Order {self.title}"
	
	class Meta:
		verbose_name = "Order"
		verbose_name_plural = "Orders"

