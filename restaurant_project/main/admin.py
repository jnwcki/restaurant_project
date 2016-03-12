from django.contrib import admin
from main.models import UserProfile, Restaurant, Item, Menu, Order


admin.site.register(UserProfile)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Order)
