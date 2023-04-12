from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from . models import *
from courses.models import Course
from store.models import Product
from math import ceil
from store.utils import cartData
from django.views import generic
from .forms import CommentForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    posts = Post.objects.filter(status='published')
    courses = Course.objects.filter(active=True)
    products = Product.objects.filter(category='book')
    mproducts = Product.objects.filter(category='merch')

    context = {
        'cartItems':cartItems,
        'posts':posts,
        'courses':courses,
        'products':products,
        'mproducts':mproducts
    }
    return render(request, 'blog/home.html', context)

def blog(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'posts' : Post.objects.filter(status='published'),
        'cartItems':cartItems
    }
	
    return render(request, 'blog/blog.html', context)

def blogpost(request, post):
    post = get_object_or_404(Post, slug=post)
    comments = post.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect('/blog/' + post.slug)
    else:
        comment_form = CommentForm()

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form,
        'cartItems':cartItems
    }

    return render(request, 'blog/blogpost.html', context)


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('Home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'blog/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            next_page = request.GET.get('next')
            
            if user is not None:
                login(request, user)
                 
                if next_page is not None:
                    return redirect(next_page)
                    
                else:
                	return redirect('Home')
                    
            else:
                messages.info(request, 'Username OR password is incorrect')
                
        context = {}
        return render(request, 'blog/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')