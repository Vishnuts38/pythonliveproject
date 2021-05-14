from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import vend
from product.models import Category,Subcategory
from client.models import User,order,order_details
from .serializers import vend_serializer,category_serializer,subcategory_serializer,User_serializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

# vendor crud operations
@api_view()
def vendisp(request):
    a=vend.objects.all()
    b=vend_serializer(a,many=True)
    return Response(b.data)

@api_view(['POST'])
def insert(request): 
    if request.method =='POST':
        em=request.data.get('email')
        br=request.data.get('branch')
        nm=request.data.get('name')
        ur=request.data.get('url')
        ps=request.data.get('password')
        ad=request.data.get('address')
        ph=request.data.get('phone')
        gs=request.data.get('gst')
        k=vend(email=em,branch=br,name=nm,url=ur,password=ps,address=ad,phone=ph,gst=gs)
        k.save() 
        ob=vend.objects.all()
        d=vend_serializer(ob,many=True)
        return Response(d.data) 
    return Response("fill")

@api_view(['POST'])
def find_name(request):
    a=vend.objects.all()
    b=vend_serializer(a,many=True)
    if request.method=='POST':
        se=request.data.get('name')
        c=vend.objects.filter(name=se)
        d=vend_serializer(c,many=True)
        return Response(d.data)
    return Response(b.data)

@api_view(['GET','POST'])
def ven_del(request,userid):
    d=vend.objects.get(id=userid)
    d.delete()
    return Response("user"+d.name+"is deleted")

@api_view(['POST'])
def ven_up(request,userid):
    k=vend.objects.filter(id=userid).values()
    if request.method=='POST':
        
        em=request.data.get('email')
        br=request.data.get('branch')
        nm=request.data.get('name')
        ur=request.data.get('url')
        ps=request.data.get('password')
        ad=request.data.get('address')
        ph=request.data.get('phone')
        gs=request.data.get('gst')
        k.update(email=em,branch=br,name=nm,url=ur,password=ps,address=ad,phone=ph,gst=gs)
        c=vend.objects.all()
        b=vend_serializer(c,many=True)
        return Response(b.data)
    return Response("updated")


# category crud operations
@api_view()
def catdisp(request):
    a=Category.objects.all()
    b=category_serializer(a,many=True)
    return Response(b.data)

@api_view(['POST'])
def catadd(request): 
  if request.method =='POST':
       
       cn=request.data.get('Category_Name')
       im=request.data.get('Image')
       cd=request.data.get('Category_Desc')
       ve=request.data.get('vend')
       k=Category(Category_Name=cn,Image=im,Category_Desc=cd,vendname=ve)
       k.save() 
       ob=Category.objects.all()
       d=category_serializer(ob,many=True)
       return Response(d.data) 
  return Response("fill") 

@api_view(['GET','POST'])
def catdel(request,userid):
    d=Category.objects.get(id=userid)
    d.delete()
    return Response("deleted")

@api_view(['POST'])
def catupdate(request,userid):
    k=Category.objects.filter(id=userid).values()
    if request.method=='POST':
        
        cn=request.data.get('Category_Name')
        im=request.data.get('Image')
        cd=request.data.get('Category_Desc')
        ve=request.data.get('vend')
        k.update(Category_Name=cn,Image=im,Category_Desc=cd,vend=ve)
        c=Category.objects.all()
        b=category_serializer(c,many=True)
        return Response(b.data)
    return Response("updated")


# sub-category crud operations
@api_view()
def subcatdisp(request):
    a=Subcategory.objects.all()
    b=subcategory_serializer(a,many=True)
    return Response(b.data)

@api_view(['POST'])
def subcatadd(request): 
  if request.method =='POST':
       
       sn=request.data.get('Subcategory_Name')
       im=request.data.get('Image')
       sd=request.data.get('Subcategory_Desc')
       ca=request.data.get('Category')
       ve=request.data.get('vend')
       k=Category(Subcategory_Name=sn,Image=im,Subcategory_Desc=sd,Category=ca,vend=ve)
       k.save() 
       ob=Subcategory.objects.all()
       d=subcategory_serializer(ob,many=True)
       return Response(d.data) 
  return Response("fill") 

@api_view(['POST'])
def subcatdel(request,userid):
    d=Subcategory.objects.get(id=userid)
    d.delete()
    return Response("user"+d.Subcategory_Name+"is deleted")

@api_view(['POST'])
def subcatupdate(request,userid):
    k=Subcategory.objects.filter(id=userid).values()
    if request.method=='POST':
        
        sn=request.data.get('Subcategory_Name')
        im=request.data.get('Image')
        sd=request.data.get('Subcategory_Desc')
        ca=request.data.get('Category')
        ve=request.data.get('vend')
        k.update(Subcategory_Name=sn,Image=im,Subcategory_Desc=sd,Category=ca,vend=ve)
        c=Subcategory.objects.all()
        b=subcategory_serializer(c,many=True)
        return Response(b.data)
    return Response("updated")

