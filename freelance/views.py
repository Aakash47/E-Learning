from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import *
from store.utils import cartData
from .forms import FcontactForm

# Create your views here.

def freelance(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    freelancers = Freelance.objects.all()
    context ={
        'cartItems':cartItems,
        'freelancers':freelancers,
    }
    print(freelancers)

    return render(request, 'freelance.html', context)

def freelancepage(request, slug):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    freelance = get_object_or_404(Freelance, slug=slug)

    if request.method == 'POST':
        fcontact_form = FcontactForm(request.POST)
        if fcontact_form.is_valid():
            fcontact_form.instance.user = request.user.customer
            fcontact_form.instance.freelance = freelance
            fcontact_form.save()
            return redirect('/freelance/' + freelance.slug)
    else:
        fcontact_form = FcontactForm()
    context = {
        'cartItems':cartItems,
        'freelance':freelance,
        'fcontact_form':fcontact_form,
    }
    return render(request, 'freelancepage.html', context)

# def contfreelancer(request):

#     data = cartData(request)

#     cartItems = data['cartItems']
#     order = data['order']
#     items = data['items']

#     if request.method == 'POST':
#         fcontact_form = FcontactForm(request.POST)
#         if fcontact_form.is_valid():
#             fcontact_form.instance.user = request.user.customer
#             fcontact_form.save()
#     else:
#         fcontact_form = FcontactForm()

#     context ={
#         'cartItems':cartItems,
#         'fcontact_form':fcontact_form,
#     }

#     return render(request, 'contfreelancer.html', context)