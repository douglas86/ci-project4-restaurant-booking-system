# Register your models here.
from django.contrib import admin

from .form import ChefForm
from .models import ChefSpecial


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
