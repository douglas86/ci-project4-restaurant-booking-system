# Register your models here.
from django.contrib import admin

from .models import Customers


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    """
    Custom Admin Panel for Customers Model
    """
    pass
