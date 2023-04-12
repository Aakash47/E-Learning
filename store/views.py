from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
from .utils import cartData
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime
from Elearning.settings import KEY_ID, KEY_SECRET
from time import time
from . models import *
from . forms import ShippingInfo
import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

# Create your views here.
def book(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'products' : Product.objects.filter(category='book'),
        'cartItems':cartItems
    }
    return render(request, 'book.html', context)

def merch(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'products' : Product.objects.filter(category='merch'),
        'cartItems':cartItems
    }
    return render(request, 'merch.html', context)

def storeview(request, slug):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'product' : get_object_or_404(Product, slug=slug),
        'cartItems':cartItems
    }
    return render(request, 'storeview.html', context)

@login_required(login_url='/login/')
def cart(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order,'cartItems':cartItems}
    return render(request, 'cart.html', context)

@login_required(login_url='login')
def checkout(request):

    transaction_id = datetime.datetime.now().timestamp()
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    if request.method == 'POST':
        form = ShippingInfo(request.POST)
        if form.is_valid() :
            form.instance.order= order
            form.instance.customer = request.user.customer
            form.save()
    else:
         form = ShippingInfo()

    if order.get_cart_items == 0 :
        return redirect(cart)

    user = request.user.customer
    action = request.GET.get('action')
    razorpay_order = None

    amount = order.get_cart_total * 100

    if action == 'create_payment':

        currency = "INR"
        notes = {
            "email" : user.email, 
            "name" : user.name,
        }
        reciept = f"Elearning-{int(time())}"
        razorpay_order = client.order.create(
            {'receipt' :reciept , 
            'notes' : notes , 
            'amount' : amount ,
            'currency' : currency
            }
        )
        order.razorpay_order_id = razorpay_order.get('id')
        order.transaction_id = transaction_id
        order.save()
        

    context = {
        'items':items, 
        'order':order,
        'cartItems':cartItems, 
        'razorpay_order':razorpay_order, 
        'user':user,
        'form':form,
        }
    return render(request, 'checkout.html', context)

@login_required(login_url='/login')
@csrf_exempt
def verifyPayment(request):
    if request.method == "POST":
        data = request.POST
        context = {}
        print(data)
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']

            payment = Order.objects.get(razorpay_order_id = razorpay_order_id)
            payment.razorpay_payment_id  = razorpay_payment_id
            payment.payment_status =  1
            payment.complete = True
            payment.save()

            return redirect('user_order') 

        except:
            shippinginfo = ShippingAddress.objects.get(order = payment)
            shippinginfo.delete()
            return HttpResponse("Invalid Payment Details")


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    # print('Action:', action)
    # print('Product:', productId)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
        
    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    data = json.loads(request.body)
    print('process:',data)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )
    return JsonResponse('Address saved', safe=False)

def user_order(request):
    cutomer = request.user.customer
    orders = Order.objects.filter(customer=cutomer, complete=True, payment_status=1)
    order_count = orders.count()
    items=[]
    for order in orders:
        all_items = order.orderitem_set.all()
        print(all_items)
        for item in all_items:
            items.append(item)
        
    context = {
        'items':items,
        'order':orders,
        'customer':cutomer,
        'order_count':order_count,
    }
    return render(request, 'user_order.html', context)
