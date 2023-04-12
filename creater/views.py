from django.shortcuts import render, redirect, HttpResponseRedirect,HttpResponse, get_object_or_404
from django.forms import inlineformset_factory
from .forms import *
from store.models import Order, OrderItem, Customer, ShippingAddress
from courses.models import UserCourse, Course, Payment
from django.contrib.auth.decorators import login_required
from freelance.models import Fcontact

# Create your views here.
@login_required(login_url='/login')
def createrview(request):
    return render(request, 'main.html')

@login_required(login_url='/login')
def addblog(request):
    if request.method == 'POST':
        addblogs = AddblogForm(request.POST, request.FILES or None)
        if addblogs.is_valid():
            addblogs.instance.author = request.user
            addblogs.save()
            return redirect('createrblogs')
    else:
        addblogs = AddblogForm()
    context = {
        'addblogs':addblogs,
    }
    return render(request, 'addblog.html', context)

@login_required(login_url='/login')
def addcourse(request):
    # Courses = inlineformset_factory(Course, Video, fields=('title','serial_number','video_id', 'is_preview'))
    # courseform = Courses()
    addcourses = AddcourseForm(request.POST, request.FILES or None)

    tagform = inlineformset_factory(Course, Tag, fields=('description',),can_delete=True,extra=1)
    addtags = tagform(request.POST)

    preform = inlineformset_factory(Course, Prerequisite, fields=('description',),can_delete=True,extra=1)
    addpre = preform(request.POST)

    learnform = inlineformset_factory(Course, Learning, fields=('description',),can_delete= True,extra=1)
    addlearn = learnform(request.POST)

    # addvideos = AddvideoForm(request.POST)
    addvideoform = inlineformset_factory(Course,Video, fields=('title', 'serial_number', 'video_id', 'is_preview'), can_delete=False ,extra= 10 )
    formset = addvideoform(request.POST, queryset=Video.objects.none())
    if request.method == "POST":
        courses_valid = addcourses.is_valid()
        tags_valid = addtags.is_valid()
        pre_valid = addpre.is_valid()
        learn_valid = addlearn.is_valid()
        # videos_valid = addvideos.is_valid()
        formset_valid = formset.is_valid()
        if courses_valid and tags_valid and pre_valid and learn_valid and formset_valid:
            addcourses.instance.seller = request.user.customer
            
            courses = addcourses.save()

            addtag = addtags.save(commit=False)
            for tagform in addtag:
                tagform.course = courses
                tagform.save()

            addpres = addpre.save(commit=False)
            for tagpre in addpres:
                tagpre.course = courses
                tagpre.save()

            addlearns = addlearn.save(commit=False)
            for taglearn in addlearns:
                taglearn.course = courses
                taglearn.save()
            
            formsets = formset.save(commit=False)
            for form in formsets:
                form.course = courses
                form.save()

            return redirect('creatercourse')
               
    else:
        addcourses = AddcourseForm()
        addtags = tagform()
        addpre = preform()
        addlearn = learnform()
        # addvideos = AddvideoForm()
        formset = addvideoform()
    
    context = {
        # 'courseform':courseform,
        'addcourses':addcourses,
        'addtags':addtags,
        # 'addvideos':addvideos,
        'addlearn':addlearn,
        'addpre':addpre,
        'formset':formset,
    }
    return render(request, 'addcourse.html', context)

@login_required(login_url='/login')
def addproduct(request):
    if request.method == 'POST':
        addproducts = AddproductForm(request.POST, request.FILES or None)
        if addproducts.is_valid():
            addproducts.instance.seller = request.user.customer
            addproducts.save()
            return redirect('createrproducts')
    else:
        addproducts = AddproductForm()
    context = {
        'addproducts':addproducts,
    }
    return render(request, 'addproduct.html', context)

@login_required(login_url='/login')
def addfreelance(request):
    addfreelances = AddfreelanceForm(request.POST, request.FILES or None)
    # addprojects = AddprojectForm()
    addprojects = inlineformset_factory(Freelance, Projects, fields=('skills','projects_done'), can_delete=False , widgets = {'projects_done':forms.Textarea(attrs={'rows':5, 'cols':50})},extra=1)
    formset = addprojects(request.POST, queryset=Projects.objects.none())
    if request.method == "POST":
        freelances_valid = addfreelances.is_valid()
        formset_valid = formset.is_valid()
        if freelances_valid and formset_valid:
            addfreelances.instance.user = request.user.customer
            freelances = addfreelances.save()
            formsets = formset.save(commit = False)
            for form in formsets:
                form.freelance = freelances
                form.save()
            return redirect('createrfreelances')
    else:
        addfreelances = AddfreelanceForm()
        formset = addprojects
        
    context = {
        'addfreelances':addfreelances,
        # 'addprojects':addprojects,
        'formset':formset,
    }
    return render(request, 'addfreelance.html', context)

@login_required(login_url='/login')
def createrblog(request):
    customer = request.user
    blogs = Post.objects.filter(author=customer)

    context = {
        'customer':customer,
        'blogs':blogs,
    }
    return render(request, 'createrblogs.html', context)

@login_required(login_url='/login')
def creatercourse(request):
    customer = request.user.customer
    courses = Course.objects.filter(seller=customer)

    context = {
        'customer':customer,
        'courses':courses,
    }
    return render(request, 'creatercourse.html', context)

@login_required(login_url='/login')
def createrproduct(request):
    customer = request.user.customer
    products = Product.objects.filter(seller=customer)

    context = {
        'customer':customer,
        'products':products
    }
    return render(request, 'createrproducts.html', context)

@login_required(login_url='/login')
def createrfreelance(request):
    customer = request.user.customer
    freelances = Freelance.objects.filter(user=customer)

    context = {
        'customer':customer,
        'freelances':freelances,
    }
    return render(request, 'createrfreelance.html', context)

@login_required(login_url='/login')
def updateblogs(request, post):
    post = get_object_or_404(Post, slug=post)
 
    if request.method == 'POST':
        updateblog = AddblogForm(request.POST or None, request.FILES or None, instance=post)
        if updateblog.is_valid():
            updateblog.save()
            return redirect('createrblogs')
    else:
        updateblog = AddblogForm(instance=post)

    context = {
        'post':post,
        'updateblog':updateblog,
    }
    return render(request, 'updateblog.html', context)

@login_required(login_url='/login')
def deleteblog(request, post):
    post = get_object_or_404(Post, slug=post)
    post.delete()
    return redirect('createrblogs')

@login_required(login_url='/login')
def updatecourse(request, slug):
    course = get_object_or_404(Course, slug=slug)
    # tags = get_object_or_404(Tag, course=course)
    # pre = get_object_or_404(Prerequisite, course=course)
    # learn = get_object_or_404(Learning, course=course)

    updatecourses = AddcourseForm(request.POST, request.FILES or None, instance=course)
    
    tagform = inlineformset_factory(Course, Tag, fields=('description',),can_delete=True,extra=1)
    updatetags = tagform(request.POST, instance=course)

    preform = inlineformset_factory(Course, Prerequisite, fields=('description',),can_delete=True,extra=1)
    updatepre = preform(request.POST, instance=course)

    learnform = inlineformset_factory(Course, Learning, fields=('description',),can_delete=True,extra=0)
    updatelearn = learnform(request.POST, instance=course)

    updatevideoform = inlineformset_factory(Course,Video, fields=('title', 'serial_number', 'video_id', 'is_preview'), can_delete=False ,extra= 10 )
    formset = updatevideoform(request.POST,instance=course)

    if request.method == "POST":
        courses_valid = updatecourses.is_valid()
        tags_valid = updatetags.is_valid()
        pre_valid = updatepre.is_valid()
        learn_valid = updatelearn.is_valid()
        formset_valid = formset.is_valid()
        if courses_valid and tags_valid and pre_valid and learn_valid and formset_valid:
            updatecourses.instance.seller = request.user.customer

            courses = updatecourses.save()

            updatetag = updatetags.save(commit=False)
            for tagform in updatetag:
                tagform.course = courses
                tagform.save()

            updatepres = updatepre.save(commit=False)
            for tagpre in updatepres:
                tagpre.course = courses
                tagpre.save()

            updatelearns = updatelearn.save(commit=False)
            for taglearn in updatelearn:
                taglearn.course = courses
                taglearn.save()

            formsets = formset.save(commit = False)
            for form in formsets:
                form.course = courses
                form.save()

            return redirect('creatercourse')
    else:
        updatecourses = AddcourseForm(instance=course)
        updatetags = tagform(instance=course)
        updatepre = preform(instance=course)
        updatelearn = learnform(instance=course)
        # addvideos = AddvideoForm()
        formset = updatevideoform(instance=course)
    
    context = {
        # 'course':course,
        'updatecourses':updatecourses,
        'updatetags':updatetags,
        'updatepre':updatepre,
        'updatelearn':updatelearn,
        # 'updatevideo':updatevideo,
        'formset':formset,
    }
    return render(request, 'updatecourse.html', context)

@login_required(login_url='/login')
def updateproduct(request, slug):
    products = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        updateproduct = AddproductForm(request.POST or None, request.FILES or None, instance=products)
        if updateproduct.is_valid():
            updateproduct.save()
            return redirect('createrproducts')
    else:
        updateproduct = AddproductForm(instance=products)
    
    context = {
        'products':products,
        'updateproduct':updateproduct,
    }
    return render(request, 'updateproduct.html', context)

@login_required(login_url='/login')
def updatefreelance(request, slug):
    freelances = get_object_or_404(Freelance, slug=slug)

    updatefreelances = AddfreelanceForm(request.POST, request.FILES or None, instance=freelances)
    # addprojects = AddprojectForm()
    updateprojects = inlineformset_factory(Freelance, Projects, fields=('skills','projects_done'), can_delete=False , widgets = {'projects_done':forms.Textarea(attrs={'rows':5, 'cols':50})},extra=0)
    formset = updateprojects(request.POST, instance=freelances)
    if request.method == "POST":
        freelances_valid = updatefreelances.is_valid()
        formset_valid = formset.is_valid()
        if freelances_valid and formset_valid:
            updatefreelances.instance.user = request.user.customer
            freelances = updatefreelances.save()
            formsets = formset.save(commit=False)
            for form in formsets:
                form.freelance = freelances
                form.save()
            return redirect('createrfreelances')
    else:
        updatefreelances = AddfreelanceForm(instance=freelances)
        formset = updateprojects(instance=freelances)

    context = {
        'updatefreelances':updatefreelances,
        'formset':formset,
    }
    
    return render(request, 'updatefreelance.html', context)

@login_required(login_url='/login')
def sellerorder(request):
    user = request.user.customer
    orders = Order.objects.filter(complete=True, payment_status=1)
    order_count = orders.count()
    items=[]
    citems=[]
    fitems=[]
    adds=[]

    for order in orders:
        ordersell = Product.objects.filter(seller=user)
        
        for sellorder in ordersell:
            all_items = order.orderitem_set.filter(product=sellorder)

            for item in all_items:
                items.append(item)

        # address = order.shippingaddress_set.filter(order=order)
        address = ShippingAddress.objects.filter(order=order)
        for add in address:
            adds.append(add)
        

    scourses = Course.objects.filter(seller=user)
    # pay = Payment.objects.filter(course=scourses)
    for secourse in scourses:
        encourses = Payment.objects.filter(course=secourse, status=True)

        for citem in encourses:
            citems.append(citem)

    freelance = Freelance.objects.filter(user=user)
    
    for sfreelance in freelance:
        fcontact = Fcontact.objects.filter(freelance=sfreelance)

        for fitem in fcontact:
            fitems.append(fitem)


    context = {
        'items':items,
        'order':orders,
        'order_count':order_count,
        'ordersell':ordersell,
        'citems':citems,
        'scourses':scourses,
        'fitems':fitems,
        'freelance':freelance,
        'address':address,
        'adds':adds,
        
    }

    return render(request, 'dashboard.html', context)

