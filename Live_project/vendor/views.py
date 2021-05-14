from django.shortcuts import render,redirect
from product.models import Category,Subcategory,Product
from vendor.models import vend
from client.models import User,order,order_details
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required

    

def reg(request):
    
    if request.method=='POST':
        
        
        un=request.POST.get("username")
        fn=request.POST.get("firstname")
        ln=request.POST.get("lastname")
        ps=request.POST.get("password")
        ce=request.POST.get("email")
        im1=request.FILES["image"]
        f1=FileSystemStorage()
        fr1=f1.save(im1.name,im1)
        
        k=User.objects.create_user(Image=fr1,username=un,first_name=fn,last_name=ln,email=ce,password=ps)
        # Token.objects.create(user=k)
        return redirect('log')
    return render (request,"register.html")

def loginuser(request):
    if request.method == 'POST':
        
        
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            
            
            
            if user is not None:
                login(request, user)
                request.session['email'] = email
               
               
                return render(request,"index.html")
            else:
                return HttpResponse("Invalid username or password!!!!!!")
       
   
    return render(request,"login.html")


   

def cat(request):
    k=Category.objects.all()
    v=vend.objects.all()
    if request.method=='POST':
        na=request.POST.get('cname')
        des=request.POST.get('description')
        va=request.POST.get('vendor')
        ve=vend.objects.get(vname=va)
        im=request.FILES["image"]
        f1=FileSystemStorage()
        fr=f1.save(im.name,im)
        re=Category(Category_Name=na,Category_Desc=des,Image=fr,vendname=ve)
        re.save()
        return render(request,'category.html',{'vat':v,'datas':k})
    return render(request,'category.html',{'vat':v,'datas':k})

def logedout(request):
    logout(request)
    return render(request,'login.html')
        
def prod(request):
    k=Product.objects.all()
    c=Category.objects.all()
    sc=Subcategory.objects.all()
    if request.method=='POST':
        na=request.POST.get('pname')
        ca=request.POST.get('category')
        ce=Category.objects.get(Category_Name=ca)
        sa=request.POST.get('subcategory')
        se=Subcategory.objects.get(Subcategory_Name=sa)
        desc=request.POST.get('description')
        pr=request.POST.get('price')
        st=request.POST.get('stock')
        ss=request.POST.get('stockstatus')
        im1=request.FILES['image1']
        f1=FileSystemStorage()
        fr1=f1.save(im1.name,im1)
        
        pro=Product(Name=na,Category=ce,Subcategory=se,Stock=st,Stock_status=ss,Product_Desc=desc,Price=pr,Image1=fr1)
        pro.save()
    return render(request,'product.html',{'cat':c,'scat':sc,'datas':k})

def searchname(request):
    d=Product.objects.all()
    if request.method=='POST':
        se=request.POST.get('search')
        d=Product.objects.filter(Name=se)
        return render(request,"product.html",{'datas':d})
    return render(request,"product.html",{'datas':d})

def searchcat(request):
    d=Category.objects.all()
    if request.method=='POST':
        se=request.POST.get('search')
        d=Category.objects.filter(Category_Name=se)
        return render(request,"category.html",{'datas':d})
    return render(request,"category.html",{'datas':d})

def delpro(request,prodid):
    k=Product.objects.get(id=prodid)
    k.delete()
    return redirect('pro') 

def delcat(request,catid):
    k=Category.objects.get(id=catid)
    k.delete()
    return redirect('cat') 

def updatepro(request,prodid):
    k=Product.objects.filter(id=prodid).values()
    c=Category.objects.all()
    sc=Subcategory.objects.all()
    if request.method=='POST':
        na=request.POST.get('pname')
        ca=request.POST.get('category')
        ce=Category.objects.get(Category_Name=ca)
        sa=request.POST.get('subcategory')
        se=Subcategory.objects.get(Subcategory_Name=sa)
        desc=request.POST.get('description')
        pr=request.POST.get('price')
        st=request.POST.get('stock')
        ss=request.POST.get('stockstatus')
        im1=request.FILES['image1']
        f1=FileSystemStorage()
        fr1=f1.save(im1.name,im1)
        k.update(Name=na,Category=ce,Subcategory=se,Stock=st,Stock_status=ss,Product_Desc=desc,Price=pr,Image1=fr1)
        return redirect('pro')
    return render(request,"update.html",{'k':k[0],'id':prodid,'cat':c,'scat':sc})

def updatecat(request,catid):
    k=Category.objects.filter(id=catid).values()
    v=vend.objects.all()
    if request.method=='POST':
        na=request.POST.get('cname')
        des=request.POST.get('description')
        va=request.POST.get('vendor')
        ve=vend.objects.get(vname=va)
        im=request.FILES["image"]
        f1=FileSystemStorage()
        fr=f1.save(im.name,im)
        k.update(Category_Name=na,Category_Desc=des,Image=fr,vendname=ve)
        return redirect('cat')
    return render(request,"updatecat.html",{'k':k[0],'id':catid,'vat':v})

def searchprice(request):
    d=Product.objects.all()
    if request.method=='POST':
        se1=request.POST.get('search1')
        se2=request.POST.get('search2')
        d=Product.objects.filter(Price__range=(se1,se2))
        return render(request,"product.html",{'datas':d})
    return render(request,"product.html",{'datas':d})