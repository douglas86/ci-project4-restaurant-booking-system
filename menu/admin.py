# Register your models here.

from django.contrib import admin

from menu.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Class to register the menu on the admin dashboard
    It will register as Menu and not MenuAdmin
    """

    # fields that I want to see on the admin panel
    list_display = ("title", "description", "served", "created_at", "updated_at")
    # I want to search based on title
    search_fields = ("title",)
