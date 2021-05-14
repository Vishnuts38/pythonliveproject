from django.db import models
from vendor.models import vend
from django.contrib.auth.models import User


class Category(models.Model):  
  
  Category_Name=models.CharField(max_length=50,null=True) 
  Image=models.ImageField(upload_to ='product/',null=True,blank=True)
  Category_Desc=models.CharField(max_length=150,null=True)  
  vendname=models.ForeignKey(vend, on_delete=models.CASCADE,null=True)

  def __str__(self):
     return self.Category_Name
 
class Subcategory(models.Model):  
  
  Subcategory_Name=models.CharField(max_length=50,null=True) 
  Image=models.ImageField(upload_to ='product/',null=True,blank=True)
  Subcategory_Desc=models.CharField(max_length=150,null=True)  
  Category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
  vendname=models.ForeignKey(vend, on_delete=models.CASCADE,null=True)
  def __str__(self):
   return self. Subcategory_Name


class Product(models.Model):
   
    Name=models.CharField(max_length=30,null=True) 
    Image1=models.ImageField(upload_to ='product/',null=True,blank=True)   
    # Image2=models.ImageField(upload_to ='product/',null=True,blank=True)   
    # Image3=models.ImageField(upload_to ='product/',null=True,blank=True)   
    Product_Desc=models.CharField(max_length=150,null=True)  
    Price=models.FloatField(null=True) 
    Stock=models.IntegerField(null=True) 
    Category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    Subcategory=models.ForeignKey(Subcategory, on_delete=models.CASCADE,null=True)
    Stock_status=models.CharField(max_length=30,null=True) 
    vendname=models.ForeignKey(vend, on_delete=models.CASCADE,null=True)
    
    def __str(self):    
      return self.Name
