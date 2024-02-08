# Register your models here.
from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'next_booking', 'table_history', 'role', 'created_at', 'updated_at')
    search_fields = ('user_name',)
