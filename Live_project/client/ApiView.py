# from rest_framework.response import Response

# from django.shortcuts import render ,redirect

# from rest_framework.decorators import api_view,permission_classes

# from rest_framework.permissions import IsAuthenticated

# from .models import User,order,order_details

# from vendor.models import vend

# from product.models import *

# from .serializers import User_serializer,order_serializer,order_details_serializer

# from django.contrib.auth import authenticate,login

# from rest_framework.authtoken.models import Token

# from rest_framework.authtoken.views import ObtainAuthToken

# #*******************************Display customers*******************************************************#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def customerdisplay(request):
#     a=User.objects.all()
#     b=User_serializer(a,many=True)
#     return Response(b.data)


# #************************ ***********signup  Customers*********************************************************#

# @api_view(['POST','GET'])

# def signupcustomer(request):
    
#     if request.method=='POST':
        
#         img=request.data.get("Image")
#         un=request.data.get("username")
#         fn=request.data.get("first_name")
#         ln=request.data.get("last_name")
#         ps=request.data.get("password")
#         ce=request.data.get("email")
#         pn=request.data.get("phone")
#         ad=request.data.get("address")
#         cty=request.data.get("city")
#         pc=request.data.get("postcode")
        
#         k=User.objects.create_user(Image=img,username=un,first_name=fn,last_name=ln,email=ce,phone=pn,address=ad,city=cty,postcode=pc,password=ps)
#         Token.objects.create(user=k)
#         u=User.objects.all()
#         s=User_serializer(u,many=True)
        
#         return Response(data={'email':k.email,'token':Token.objects.get(user=k).key,'response':"sucessfully registred user!!!!"})
        
  

#     return Response("please fill the form ")

# #*************************Delete customers****************************************************************8#
# @api_view(['POST'])
# def deletecustomer(request,userid):
#     d=User.objects.get(id=userid)
#     d.delete()
#     return Response("username  "+d.username+" is deleted")

# #****************************Update customers**************************************************************#
# @api_view(['POST','GET'])
# def updatecustomer(request,userid):
#     u=User.objects.filter(id=userid).values()
#     if request.method=='POST':
        
#         img=request.data.get("Image")
#         un=request.data.get("username")
#         fn=request.data.get("first_name")
#         ln=request.data.get("last_name")
#         em=request.data.get("email")
#         ce=request.data.get("email")
#         pn=request.data.get("phone")
#         ad=request.data.get("address")
#         cty=request.data.get("city")
#         pc=request.data.get("postcode")
        
#         u.update(Image=img,username=un,first_name=fn,last_name=ln,email=ce,phone=pn,address=ad,city=cty,postcode=pc)
#         k=User.objects.all()
#         s=User_serializer(k,many=True)
#         return Response(s.data)
#     return Response("username  "+u.username+" is updated")
# #***********************************login customer**************************************#
# @api_view(['POST','GET'])
# def customerlogin(request):
    
#     if request.method=='POST':
#         em=request.POST.get("email")
#         ps=request.POST.get("password")
#         user=authenticate(request,email=em,password=ps)
       
#         if user :
#             v=Token.objects.get(user=user)
#             login(request,user)
            

#             return Response(data={'email':user.email,'token':v.key})   
        
#         return Response("invalid user!!!!")
     

# #************************************singup2****************************************
# @api_view(['POST'])
# def signupView(request):
# 	if request.method == 'POST':
# 		username = request.data.get('email')
# 		password = request.data.get('password')
# 		u = User.objects.create_user(email = username,password = password)
# 		return Response(data = {'username':u.email,'response':'Successfully registered a user'})

# #***********************************Create Oder*************************************#
# @api_view(['POST','GET'])

# def createorder(request):
    
#     if request.method=='POST':
#         pid=request.data.get("Product_id")
#         spid=Product.objects.get(Name=pid)
#         pqy=request.data.get("Product_Qty")
#         pp=spid.Price
        
#         stt=int (pqy)* int (pp)
        
        
#         if spid.Stock<=0:
#             return Response("Out of Stock")
#         else:
#             spid.Stock-=int (pqy)
#             spid.save()
            
#             ordat=request.data.get("Order_date") 
#             ortot=request.data.get("Order_total")  
#             deldat=request.data.get("Delivery_date")
#             isdel=request.data.get("Is_delivered")
#             paymet=request.data.get("Payment_method")
#             paysts=request.data.get("Payment_Status")
#             cid=request.data.get("Customer_id")
#             scid=User.objects.get(username=cid)
#             vid=request.data.get("vend_id")
#             svid=vend.objects.get(vname=vid)
#             sts=request.data.get("status")
#             k=order.objects.create(Order_date=ordat,Order_total=ortot,Delivery_date=deldat,Is_delivered=isdel,Payment_method=paymet,Payment_Status=paysts,Customer_id=scid,vend_id=svid,status=sts)
#             order_details.objects.create(Product_id=spid,Product_Qty=pqy,Product_Price=pp,Subtotal=stt,Order=k)
#     o=order.objects.all()
#     od=order_details.objects.all()
#     #ods=order_details_serializer(od,many=True)
#     os=order_serializer(o,many=True)
#     return Response(os.data)
#     #return Response(ods.data)
    

# #************************************show all oders*****************************************************#
# @api_view(['GET'])
# def showallorders(request):
#     a=order.objects.all()
#     b=order_serializer(a,many=True)
#     return Response(b.data)

# #***********************************orders filter by ordered date ***********************************************#
# @api_view(['POST','GET'])
# def orderbydate(request):
#     d=order.objects.all()
#     fd=order_serializer(d,many=True)
#     if request.method=='POST':
        
#         s1=request.data.get("L1")
#         s2=request.data.get("L2")
#         d=order.objects.filter(Order_date__range=(s1,s2))
#         fd=order_serializer(d,many=True)
#         return Response(fd.data)
#     return Response(fd.data)
    

# #***********************************orders filter by deliverd  date ***********************************************#
# @api_view(['POST','GET'])
# def deliverybydate(request):
#     fd=order.objects.all()
#     sfd=order_serializer(fd,many=True)
#     if request.method=='POST':
#         s1=request.data.get("L1")
#         s2=request.data.get("L2")
#         fd=order.objects.filter(Delivery_date__range=(s1,s2))
#         sfd=order_serializer(fd,many=True)
#         return Response(sfd.data)
#     return Response(sfd.data)
# #*************************************orders by a user by username***************************************************#
# @api_view(['GET'])
# def orderbyusername(request,userid):
#     v=User.objects.filter(username=userid)
#     kes=User_serializer(v,many=True)
#     return Response(kes.data)

# # #*************************************orders by a user by email***************************************************#
# @api_view(['POST'])
# def orderbyemail(request):
#     un=order.objects.all()
#     sun=order_serializer(un,many=True)
#     if request.method=='POST':
#         k=request.data.get("email")
#         ke=order.objects.filter(Customer_id__in=User.objects.filter(email=k)).distinct()
#         print(ke)
#         kes=order_serializer(ke,many=True)
#         return Response(kes.data)
#     return Response(kes.data)
# #**************************************orders by status ***********************************************************#
# @api_view(['POST'])
# def orderbystatus(request):
#     ct=order.objects.all()
#     sct=order_serializer(ct,many=True)
#     if request.method=='POST':
#         c=request.data.get("status")
#         ce=order.objects.filter(status=c)
#         ces=order_serializer(ce,many=True)
#         return Response(ces.data)
#     return Response(ces.data)
#******************************************************edit order**********************************************************#
def editorder(request,orid,odid):
    k=order.objects.filter(id=orid).values()
    p=order_details.objects.filter(id=odid).values()
    vid=vend.objects.all()
    pid=Product.objects.all()
    cid=User.objects.all()
    
    
    if request.method=='POST':
        pid=Product.objects.all()
        pid=request.POST.get("Product_id")
        spid=Product.objects.get(Name=pid)
        pqy=request.POST.get("Product_Qty")
        pp=spid.Price
        
        stt=int (pqy)* int (pp)
        
        
        if spid.Stock<=0:
            return HttpResponse("Out of Stock")
        else:
            spid.Stock-=int (pqy)
            spid.save()
            
            ordat=request.POST.get("Order_date") 
            ortot=request.POST.get("Order_total")  
            deldat=request.POST.get("Delivery_date")
            isdel=request.POST.get("Is_delivered")
            paymet=request.POST.get("Payment_method")
            paysts=request.POST.get("Payment_Status")
            
            cid=request.POST.get("Customer_id")
            scid=User.objects.get(username=cid)
            
            vid=request.POST.get("vend_id")

            svid=vend.objects.get(vname=vid)
            sts=request.POST.get("status")
            k.update(Order_date=ordat,Order_total=ortot,Delivery_date=deldat,Is_delivered=isdel,Payment_method=paymet,Payment_Status=paysts,Customer_id=scid,vend_id=svid,status=sts)
            p.update(Product_id=spid,Product_Qty=pqy)
            return redirect("addorders")
    

    return render(request,"editorder.html",{'p':p[0],'k':k[0],'id':orid,'cuid':cid,'venid':vid,'proid':pid})



