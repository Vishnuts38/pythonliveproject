from django.contrib import admin
from django.urls import path
from client import ApiView,views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('customerdisplay',ApiView.customerdisplay,name="Customerdisplay"),
    # path('addcustomer',ApiView.signupcustomer,name="Addcustomers"),
    # #path('del/<int:userid>',ApiView.deletecustomer,name="deletecustomers"),
    # #path('edit/<int:userid>',ApiView.updatecustomer,name="updatecustomers"),
    # path('customerlogin',ApiView.customerlogin,name="customerlogin"),
    # path('signup',ApiView.signupView,name="signup"),
    # path('codd',ApiView.createorder,name="createorder"),
    # path('slo',ApiView.showallorders,name="showallorders"),
    # path('fod',ApiView.orderbydate,name="odresfilterdbydate"),
    # path('dod',ApiView.deliverybydate,name="odresfilterdbydate"),
    # path('obu/<str:userid>',ApiView.orderbyusername,name="orderbyusername"),
    # path('obe',ApiView.orderbyemail,name="orderbyemail"),
    # path('obs',ApiView.orderbystatus,name="orderbystatus"),
    #*****************HTML URLS************************#
    path("ao",views.addorder,name="addorders"),
    path("odbs",views.orderbystatus,name="orderbystatus"),
    path("odbd",views.orderbydate,name="orderbydate"),
    path('delo/<int:userid>',views.deleteorder,name="delorder"),
    path('edit/<int:orid>/<int:odid>',views.editorder,name="editorder"),
    path('addusers',views.addu,name="addusers"),
    path('searchbyemail',views.searchbyemail,name="searchbyemail"),
    path('delu/<int:usid>',views.deluser,name="deleteuser")
    # path('edu/<str:edid>',views.edituser,name="edituser")
    

]

