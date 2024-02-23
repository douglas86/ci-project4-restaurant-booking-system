from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models

# Variable to use to choose what meal time the special is served
STATUS = ((0, 'Breakfast'), (1, 'Lunch'), (2, 'Supper'))


# Create your models here.
class Customer(models.Model):
    """
    Customer Model for storing data based on the user that is logged in
    """
    id = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    next_booking = models.DateField()
    table_history = models.JSONField(default=dict)
    role = models.CharField(default='customer', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String for representing the Model object by username
        :return:
        """
        return self.user_name

    class Meta:
        """
        Metaclass to order data based on the created_at in descending order
        """
        ordering = ['-created_at']


class ChefSpecial(models.Model):
    """
    Chef Specials Model for storing breakfast,
    lunch and supper for carousel on homepage
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=False, null=False)
    ingredients = models.JSONField(default=list, blank=False)
    served = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Metaclass to order data based on the served value and created_at in ascending order
        """
        ordering = ['served', 'created_at']

    def __str__(self):
        """
        String for representing the Model object by title
        :return:
        """
        return self.title
