from django.shortcuts import render

from django.shortcuts import render ,redirect

from .models import User,order,order_details

from django.http import HttpResponse

from vendor.models import vend

from product.models import *

from client.models import User

from django.core.files.storage import FileSystemStorage

#****************************create order*******************************************************************************#
def addorder(request):
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
            k=order.objects.create(Order_date=ordat,Order_total=ortot,Delivery_date=deldat,Is_delivered=isdel,Payment_method=paymet,Payment_Status=paysts,Customer_id=scid,vend_id=svid,status=sts)
            order_details.objects.create(Product_id=spid,Product_Qty=pqy,Product_Price=pp,Subtotal=stt,Order=k)
    o=order.objects.all()
    od=order_details.objects.all()
    

    return render(request,"orders.html",{'cuid':cid,'venid':vid,'proid':pid,'data':o})

    #************************************************search by payment status***************************************#
def orderbystatus(request):
    ct=order.objects.all()
    
    if request.method=='POST':
        c=request.POST.get("orderstatus")
        ct=order.objects.filter(status=c)
        
        return render(request,"orders.html",{'data':ct})
    return render(request,"orders.html",{'data':ct})

#**************************************************search by orderd date *************************************************#
def orderbydate(request):
    kt=order.objects.all()
    
    if request.method=='POST':
        
        s1=request.POST.get("s1")
        s2=request.POST.get("s2")
        print("######",s1)
        print("######",s2)
        kt=order.objects.filter(Order_date__range=(s1,s2))
        print (kt)
        return render(request,"orders.html",{'data':kt})
    return render(request,"orders.html",{'data':kt})
#*****************************************************delete order*********************************************************#
def deleteorder(request,userid):
    
    d=order.objects.get(id=userid)
    d.delete()
    return redirect("addorders")
#******************************************************edit order**********************************************************#
def editorder(request,orid,odid):
    k=order.objects.filter(id=orid).first()
    k1=order.objects.filter(id=orid).values()
    p=order_details.objects.filter(id=odid).first()
    p1=order_details.objects.filter(id=odid).values()
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
            k1.update(Order_date=ordat,Order_total=ortot,Delivery_date=deldat,Is_delivered=isdel,Payment_method=paymet,Payment_Status=paysts,Customer_id=scid,vend_id=svid,status=sts)
            p1.update(Product_id=spid,Product_Qty=pqy)
            print(k)
            return redirect("addorders")
    

    return render(request,"editorder.html",{'p':p,'k':k,'id':orid,'cuid':cid,'venid':vid,'proid':pid})

#*************************************************ADD USER**************************************************#
def addu(request):
    k=User.objects.filter(is_superuser=False)
    if request.method=='POST':
        
        im1=request.FILES["image"]
        f1=FileSystemStorage()
        fr1=f1.save(im1.name,im1)
        un=request.POST.get("username")
        rl=request.POST.get("role")
        # db=request.POST.get("dob")
        ps=request.POST.get("password")
        ce=request.POST.get("email")
        pn=request.POST.get("phone")
        ad=request.POST.get("address")
        cty=request.POST.get("city")
        pc=request.POST.get("postcode")
        
        User.objects.create_user(Image=fr1,username=un,role=rl,email=ce,phone=pn,address=ad,city=cty,postcode=pc,password=ps)
        k=User.objects.filter(is_superuser=False)
        
        # Token.objects.create(user=k)
        
        return render(request,"adduser.html",{'use':k})
    return render(request,"adduser.html",{'use':k})
        
#**********************************search by email**********************************************************#

def searchbyemail(request):
    e=User.objects.all()
    if request.method=='POST':
        s=request.POST.get("email")
        e=User.objects.filter(email=s)
        return render(request,"adduser.html",{'use':e})
    return render(request,"adduser.html",{'use':e})

#**************************************Delete user *********************************************************3
def deluser(request,usid):
    k=User.objects.get(id=usid)
    k.delete()
    return redirect("addusers")
# #**************************************edit user*************************************************************#
# def edituser(request,edid):
#     e=User.objects.get(id=edid)
#     if request.method=="POST":
#         im1=request.FILES["image"]
#         f1=FileSystemStorage()
#         fr1=f1.save(im1.name,im1)
#         un=request.POST.get("username")
#         rl=request.POST.get("role")
#         # db=request.POST.get("dob")
#         ps=request.POST.get("password")
#         ce=request.POST.get("email")
#         pn=request.POST.get("phone")
#         ad=request.POST.get("address")
#         cty=request.POST.get("city")
#         pc=request.POST.get("postcode")
        
#         e.update(Image=fr1,username=un,role=rl,email=ce,phone=pn,address=ad,city=cty,postcode=pc,password=ps)
#         e=User.objects.all()
#         return redirect("adduser")
#     return render(request,"edituser.html",{'k':e})
