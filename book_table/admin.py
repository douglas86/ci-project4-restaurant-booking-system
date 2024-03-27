# Register your models here.
from django.contrib import admin

from .form import BookTableForm
from .models import Customer, Voucher


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Custom Admin Panel for Customers Model
    """

    form = BookTableForm
    list_display = ('user', 'seats', 'time_slots', 'created_at', 'updated_at')


@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    """
    Custom Admin Panel for Vouchers Model
    """

    list_display = ('title', 'description', 'created_at')
    search_fields = ('title',)
