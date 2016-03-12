from django.contrib import admin
from main.models import UserProfile, Restaurant, Item, Menu, Order


admin.site.register(UserProfile)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Order)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'hours', 'number', 'image')

    def get_queryset(self, request):
        qs = super().queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)
