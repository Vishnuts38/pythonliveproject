from rest_framework import serializers
from .models import User,order,order_details

class order_details_serializer(serializers.ModelSerializer):
    
    class Meta:
        model=order_details
        fields='__all__'


        

class order_serializer(serializers.ModelSerializer):
    k=order_details_serializer(source='order_details_set',many=True)
    class Meta:
        model=order
        fields=['Order_date','Order_total','Delivery_date','Is_delivered','Payment_method','Payment_Status','Customer_id','vend_id','status','k']
        


class User_serializer(serializers.ModelSerializer):
    v=order_serializer(source='order_set',many=True)
    class Meta:
        model=User
        fields=['email','username','v']