from django.contrib import admin
from .models import User, Profile, Category, Product,Cart, Order, BillingAddress
# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(BillingAddress)
