from cloudinary.models import CloudinaryField

from django.contrib.auth.models import User
from django.db import models

# Variable to use to choose what meal time the special is served
STATUS = ((0, "Breakfast"), (1, "Lunch"), (2, "Supper"))


# Create your models here.
class ChefSpecial(models.Model):
    """
    Chef Specials Model for storing breakfast,
    lunch and supper for carousel on homepage
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False)
    served = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField("image", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String for representing the Model object by title
        :return:
        """
        return self.title

    class Meta:
        """
        Metaclass to order data based on the served value and created_at in ascending order
        """

        ordering = ["served", "created_at"]
