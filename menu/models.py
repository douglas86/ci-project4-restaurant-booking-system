# Create your models here.
from django.db import models

from home.models import STATUS


class Menu(models.Model):
    """
    Menu model to display the menu to template
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=False)
    description = models.TextField(blank=False)
    menu_type = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String method for representing the Model object by title
        """

        return self.title

    class Meta:
        """
        Metaclass to order data based on the updated_at in descending order
        """

        ordering = ["updated_at"]
