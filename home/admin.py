# Register your models here.
from django.contrib import admin

from .form import ChefForm
from .models import Customer, ChefSpecial


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Custom admin for the Customer
    list_display variable is used to make it easier for me in the admin panel
    search_fields variable is for searching based on user_name
    """

    list_display = (
        "user_name",
        "next_booking",
        "table_history",
        "role",
        "created_at",
        "updated_at",
    )
    search_fields = ("user_name",)


@admin.register(ChefSpecial)
class ChefSpecialAdmin(admin.ModelAdmin):
    """
    Custom admin for ChefSpecial model
    form variable is used to run validations on ChefSpecial model
    list_display variable is used to make it easier for me in the admin panel
    """

    form = ChefForm
    list_display = (
        "title",
        "description",
        "served",
        "featured_image",
        "created_at",
        "updated_at",
    )
