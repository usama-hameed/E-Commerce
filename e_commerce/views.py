from django.shortcuts import render,redirect
from e_commerce.models import User,Products
from e_commerce.forms import SignupForm,AddProductForm 
from django.contrib import messages
from django.views.generic import View,TemplateView,UpdateView
import json
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.core import serializers
# Create your views here.


products_list=[]
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            data=User.objects.get(username=username)
            print(type(data))
            if data.password==password:
                return redirect('products')
        except User.DoesNotExist:
            messages.info(request,"User Doesn't exist")
    return render(request,'login.html',{
        'messages':messages.get_messages(request)
    })

def signup(request):
    form=SignupForm()

    if request.method=='POST':
        form =SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'signup.html',{'form':form})
    

def products(request):
    
    try:

        products=Products.objects.all()
        return render(request,'products.html',{'products':products})
    except Products.DoesNotExist:
        messages.info(request,"No Products")

    return render(request,'products.html')
    

class AddProduct(FormView):
    template_name='add_product.html'
    form_class = AddProductForm
    def post(self,request):
        form=AddProductForm()
        
        if request.method=='POST':
            form=AddProductForm(request.POST)
            try:
                count=Products.objects.count()
                if count is None:
                    count=1
                else:
                    count=count+1
            except Products.DoesNotExist:


                return render(request,'add_product.html',{'form':form})
    

            if form.is_valid():
                name=form.cleaned_data['name']
                price=form.cleaned_data['price']
                new_product=Products(product_id=count,name=name,price=price)
                new_product.save()
                return redirect('products')
        return render(request,'add_product.html',{'form':form})


def UpdateProduct(request,*args,**kwargs):
    id=kwargs['id']
    form=AddProductForm()
    if request.method=='POST':
        form=AddProductForm(request.POST,instance=Products)
        if form.is_valid():
            name=form.cleaned_data['name']
            price=form.cleaned_data['price']
            Products.objects.filter(product_id=id).update(name=name,price=price)
            return redirect('products')
    return render(request,'update_product.html',{'form':form})
    

    
def DeleteProduct(request,*args,**kwargs):
    id=kwargs['id']
    Products.objects.get(product_id=id).delete()
    return redirect('products')



def ProductList(request):
    try:

        products=Products.objects.all()
    
    except:
        
        return redirect('products')

    if request.method=='POST':
        price1=request.POST.get('price1')
        price2=request.POST.get('price2')
        products=Products.objects.filter(price__gte=price1,price__lte=price2)
        return render(request,'product_list.html',{'products':products})
        
    return render(request,'product_list.html',{'products':products})


    

def AddToCart(request,*args,**kwargs):
    id=kwargs['id']
    products=Products.objects.get(product_id=id)
    
    return render(request,'add_to_cart.html')
