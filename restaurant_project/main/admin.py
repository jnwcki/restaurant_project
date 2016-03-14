from django.contrib import admin

from .models import Restaurant, UserProfile, Item, Menu, Order


admin.site.register(UserProfile)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    exclude = ('owner',)
    list_display = ('restaurant_name', 'cuisine', 'hours', 'number', 'image')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    exclude = ('owner',)
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    exclude = ('owner',)
    list_display = ('name', 'description', 'price', 'image')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    exclude = ('restaurant', 'user', 'total_price', 'notes')
    list_display = ('user', 'date', 'fulfilled', 'total_price', 'notes')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(restaurant=request.user.userprofile.owner)
