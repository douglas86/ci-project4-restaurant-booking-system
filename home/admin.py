# Register your models here.
from django.contrib import admin

from .models import Customer, ChefSpecials


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'next_booking', 'table_history', 'role', 'created_at', 'updated_at')
    search_fields = ('user_name',)


@admin.register(ChefSpecials)
class ChefSpecialsAdmin(admin):
    list_display = ('title', 'ingredients', 'served', 'featured_image', 'created_at', 'updated_at')
