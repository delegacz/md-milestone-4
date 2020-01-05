from django.contrib import admin
from .models import Item, OrderItem, Order, Payment, Address, UserProfile, Coupon
# Register your models here.

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(UserProfile)
admin.site.register(Payment)
admin.site.register(Coupon)