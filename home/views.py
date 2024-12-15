from django.shortcuts import render
from home.models import Catagory,Products
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    ct_data = Catagory.objects.all()
    # for i in ct_data:
    #     print(i.image)
    #     print("static/images/catagory/20241209235217beetroot.jpg")
    return render(request,'home.html',{'data':ct_data})

def products_catagory(request,id):
    data = Products.objects.filter(catagory_id=id)
    catagory = Catagory.objects.all()
    catagory_from_id = Catagory.objects.filter(pk=id)
    for cata_name in catagory_from_id:
        catagory_from_id = cata_name.catagory_name
    return render(request, 'products.html',{"data":data,'catagory':catagory,'display':catagory_from_id})

def products(request):
    data = Products.objects.all()
    catagory = Catagory.objects.all()
    return render(request, 'products.html',{"data":data,'catagory':catagory,"display":"All Products"})

