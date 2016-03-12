from django.contrib import admin

from .models import Restaurant, UserProfile, Item, Menu, Order


admin.site.register(UserProfile)
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Order)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'hours', 'number', 'image')

    def queryset(self, request):
        qs = super().queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)


admin.site.register(Restaurant, RestaurantAdmin)
