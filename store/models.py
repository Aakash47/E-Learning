from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	options = {
		('book','Book'),
		('merch', 'Merch'),
	}

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField()
	description = models.TextField(max_length=200, default='' , null=True , blank=True)
	image = models.ImageField(null=True, blank=True)
	slug = models.SlugField(max_length=200, unique=True, help_text='This field should be unique')
	category = models.CharField(max_length=10, choices=options, default='book')
	seller = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-date_posted',)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
class Order(models.Model):
	payment_status_choices =(
		(1,'Success'),
		(2,'Failure'),
		(3,'Pending')
	)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null= True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True, blank=True)
	transaction_id = models.CharField(max_length=200, null=True)
	razorpay_order_id = models.CharField(max_length=500,null=True,blank=True)
	payment_status = models.IntegerField(choices = payment_status_choices,default = 3)
	razorpay_payment_id= models.CharField(max_length=500,null=True,blank=True)
	# seller = models.ForeignKey(Product, on_delete=models.SET_NULL, null= True, blank=True)

	class Meta:
		ordering = ('-date_ordered',)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total



class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null= True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null= True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product.name

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null= True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null= True)
	address = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	zipcode = models.CharField(max_length=200, null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

	
