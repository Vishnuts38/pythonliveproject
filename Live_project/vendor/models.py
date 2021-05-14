from django.db import models


class vend(models.Model):
    
    vemail=models.EmailField(max_length=30,null=True)
    vbranch=models.CharField(max_length=30,null=True)
    vname=models.CharField(max_length=30,null=True)
    vurl=models.CharField(max_length=30,null=True)
    vpassword=models.CharField(max_length=30,null=True)
    vaddress=models.CharField(max_length=100,null=True)
    vphone=models.IntegerField(null=True)
    vgst=models.IntegerField(null=True)

    def __str__(self):
        return  self.vname
