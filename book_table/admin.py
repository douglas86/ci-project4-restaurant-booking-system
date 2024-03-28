# Register your models here.
from django.contrib import admin

from .form import BookTableForm
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Custom Admin Panel for Customers Model
    """

    form = BookTableForm
    list_display = ('user', 'seats', 'time_slots', 'created_at', 'updated_at')
