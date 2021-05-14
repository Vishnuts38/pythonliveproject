from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(order)
admin.site.register(order_details)