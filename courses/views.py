from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from store.models import Customer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from Elearning.settings import KEY_ID, KEY_SECRET
from time import time
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from store.utils import cartData

# Create your views here.

def courses(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    courses = Course.objects.filter(active=True)

    context ={
        'courses':courses,
        'cartItems':cartItems,
    }

    return render(request, 'courses.html', context)

def coursePage(request, slug):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    course = get_object_or_404(Course, slug=slug)
    serial_number  = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")

    if serial_number is None:
        serial_number = 1 

    video = Video.objects.get(serial_number = serial_number , course = course)

    if video.is_preview is False:

        if request.user.is_authenticated is False:
            return redirect('login')
        else:
            user = request.user.customer
            try:
                user_course = UserCourse.objects.get(user = user  , course = course)
            except:
                return redirect('check-out', slug=course.slug)

    context = {
        'course':course,
        'video':video,
        'videos':videos,
        'cartItems':cartItems,
    }
    return render(request, 'coursepage.html', context)

import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))


@login_required(login_url='/login')
def checkout(request , slug):
    course = Course.objects.get(slug = slug)
    user = request.user.customer
    action = request.GET.get('action')
    order = None
    payment = None
    error = None

    try:
        user_course = UserCourse.objects.get(user = user  , course = course)
        error = "You are Already Enrolled in this Course"
        return redirect('my_courses')
    except:
         pass

    if error is None: 
        amount =  int((course.price - ( course.price * course.discount * 0.01 )) * 100)

    if amount == 0:
        userCourse = UserCourse(user = user , course = course)
        userCourse.save()
        return redirect('my_courses')

    if action == 'create_payment':

        currency = "INR"
        notes = {
            "email" : user.email, 
            "name" : user.name,
        }
        reciept = f"Elearning-{int(time())}"
        order = client.order.create(
            {'receipt' :reciept , 
            'notes' : notes , 
            'amount' : amount ,
            'currency' : currency
            }
        )

        payment = Payment()
        payment.user  = user
        payment.course = course
        payment.order_id = order.get('id')
        payment.save()


    
    context = {
        "course" : course , 
        "order" : order, 
        "payment" : payment, 
        "user" : user , 
        "error" : error
    }
    return  render(request, 'check_out.html', context )    

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

            payment = Payment.objects.get(order_id = razorpay_order_id)
            payment.payment_id  = razorpay_payment_id
            payment.status =  True
            
            userCourse = UserCourse(user = payment.user , course = payment.course)
            userCourse.save()

            print("UserCourse" ,  userCourse.id)

            payment.user_course = userCourse
            payment.save()

            return redirect('my_courses') 

        except:
            return HttpResponse("Invalid Payment Details")

@login_required(login_url='login')
def my_courses(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    user = request.user.customer
    user_courses = UserCourse.objects.filter(user = user)
    context = {
        'user_courses' : user_courses,
        'cartItems':cartItems,
    }
    return render(request, 'my_courses.html', context)