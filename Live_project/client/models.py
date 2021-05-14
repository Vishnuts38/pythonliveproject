from django.db import models

from django.contrib.auth.models import AbstractUser,BaseUserManager

from django.contrib.auth.hashers import make_password

from vendor.models import vend

from product.models import Product

import datetime





class UserManager(BaseUserManager):
    def _create_user(self, email, password, **other_fields):
        """
        Create and save a user with the given email and password. And any other fields, if specified.
        """
        if not email:
            raise ValueError('An Email address must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **other_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **other_fields)

class User(AbstractUser):
    
    Image=models.ImageField(upload_to ='user/',null=True,blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True,null=True,blank=True)
    role=models.CharField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    postcode=models.IntegerField(null=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['address','phone','city','postcode','Image']
    objects=UserManager()

    def get_username(self):
        return self.email

class order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Ordered', 'Ordered'),
        ('Accepted', 'Accepted'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Order Cancel', 'Order Cancel'),
        ('Customer Cancel', 'Customer Cancel'),
        ('Delivered', 'Delivered'),
        ('Added to Cart', 'Added to Cart'),
        ('Assigned to Driver', 'Assigned to Driver'),
    )
    
    
    Order_date=models.DateField()
    Order_total=models.FloatField()
    Customer_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Delivery_date=models.DateField()
    Is_delivered=models.CharField(max_length=40,null=True,blank=True)
    vend_id=models.ForeignKey(vend,on_delete=models.CASCADE,null=True)  
    Payment_method=models.CharField(max_length=40,null=True,blank=True)
    Payment_Status=models.CharField(max_length=40,null=True,blank=True)
    status=models.CharField(default="ordered",max_length=50,null=True,choices=STATUS)
    
    def __str__(self):
        return str (self.Customer_id )

class order_details(models.Model):
    
    Product_id=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    Product_Qty=models.IntegerField()
    Product_Price=models.FloatField()
    Subtotal=models.IntegerField()
    Order=models.ForeignKey(order,on_delete=models.CASCADE,null=True)
    
     
    def __str__(self):
        return str (self.Product_Qty)

    

