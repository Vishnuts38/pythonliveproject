
from django.contrib import admin
from django.urls import path
from vendor import ApiView
from vendor import views

urlpatterns = [
    # vendor url
    path('admin/', admin.site.urls),
    path('vd',ApiView.vendisp,name='vd'),
    path('ins',ApiView.insert,name='ins'),
    path('sename',ApiView.find_name,name='sename'),
    path('vdel/<int:userid>',ApiView.ven_del,name='de'),
    path('ed/<int:userid>',ApiView.ven_up,name="up"),

    # category url
    path('cd',ApiView.catdisp,name='cd'),
    path('ca',ApiView.catadd,name='ca'),
    path('cdel/<int:userid>',ApiView.catdel,name='cdel'),
    path('ced/<int:userid>',ApiView.catupdate,name='ced'),

    # subcategory url
    path('subd',ApiView.subcatdisp,name='subd'),
    path('suba',ApiView.subcatadd,name='suba'),
    path('subdel/<int:userid>',ApiView.subcatdel,name='subdel'),
    path('subed/<int:userid>',ApiView.subcatupdate,name='subed'),

    # Front end url
    # path('db',views.home,name='db'),
    path('pro',views.prod,name='pro'),
    path('',views.reg,name='reg'),
    path('log',views.loginuser,name='log'),
    path('cat',views.cat,name='cat'),
    path('logedout',views.logedout,name='logout'),
    path('se',views.searchname,name='se'),
    path('seca',views.searchcat,name='seca'),
    path('prodel/<int:prodid>',views.delpro,name='del'),
    path('catdel/<int:catid>',views.delcat,name='catdel'),
    path('proup/<int:prodid>',views.updatepro,name='updatepro'),
    path('catup/<int:catid>',views.updatecat,name='updatecat'),
    path('pr',views.searchprice,name='pricerange'),



]
