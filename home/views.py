from django.shortcuts import render,redirect,get_object_or_404
from home.models import *
from home.forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    ct_data = Catagory.objects.all()
    # for i in ct_data:
    #     print(i.image)
    #     print("static/images/catagory/20241209235217beetroot.jpg")
    return render(request,'home.html',{'data':ct_data})

def products(request):
    data = Products.objects.all()
    catagory = Catagory.objects.all()
    # for item in data:
    #     print(item.catagory_id)
    return render(request, 'products.html',{"data":data,'catagory':catagory,"display":"All Products"})

def products_catagory(request,id):
    data = Products.objects.filter(catagory_id=id)
    catagory = Catagory.objects.all()
    catagory_from_id = Catagory.objects.filter(pk=id)
    for cata_name in catagory_from_id:
        catagory_from_id = cata_name.catagory_name
    return render(request, 'products.html',{"data":data,'catagory':catagory,'display':catagory_from_id})

def products_seller(request,name):
    id = User.objects.get(username = name)
    data = Products.objects.filter(seller_id=id)
    catagory = Catagory.objects.all()
    # catagory_from_id = Catagory.objects.filter(pk=id)
    # for cata_name in catagory_from_id:
    #     catagory_from_id = cata_name.catagory_name
    return render(request, 'products.html',{"data":data,'catagory':catagory,'display':name})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save(commit=True)
            user.set_password(form.cleaned_data['password'])
            form.save()
            messages.success(request,"Successfully Registered")
            return redirect('/login/')

        return render(request,'register.html',{'form':form})

    return render(request,'register.html',{'form':form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("From have POST mwethofd")
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('/home')
        return render(request,'login.html',{'form':form})

    return render(request,'login.html',{'form':form})

def logout(request):
    auth_logout(request)
    return redirect("/home")

def uploads(request):
    return render(request, "upload.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")
    
def user(request):
    user = request.user
    uid = user.id
    # Fetch the record by ID
    # profile = get_object_or_404(UserProfile, user_id=uid)
    # profile = UserProfile.objects.get(user_id=uid)
    profile = ''
    if request.method == 'POST':
        return redirect("/user_update")
    return render(request, "user.html",{'user':user,'update':True,"profile":profile})

def user_update(request):
    user = request.user
    uid = user.id
    # Fetch the record by ID
    # profile = get_object_or_404(UserProfile, user_id=uid)
    
    # profile = UserProfile.objects.get(user_id=uid)
    profile = ''
    print(request.method)
    if request.method == 'POST':
        form = UserUpdationForm(request.POST)
        # profile = UserProfile()
        print(form.is_valid())
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            form.save()
            for field in form:
                print(field)
        return render(request, 'user.html',{'form':form,"profile":profile})
    return render(request, "user.html",{"profile":profile})