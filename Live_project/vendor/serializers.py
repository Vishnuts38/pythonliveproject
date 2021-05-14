from rest_framework import serializers
from .models import vend
from product.models import Category,Subcategory
from client.models import User

class vend_serializer(serializers.ModelSerializer):
    class Meta:
        model=vend
        fields='__all__'

class category_serializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class subcategory_serializer (serializers.ModelSerializer):
    class Meta:
        model=Subcategory
        fields='__all__'

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        