from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Customer(models.Model):
    """
    Table Bookings for when the customer wants to book at the restaurant
    """

    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField(blank=False, null=False,
                                        validators=[MinValueValidator(1), MaxValueValidator(10)])
    time_slots = models.DateTimeField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        I want to display data based on user_name
        :return:
        """

        return str(self.user)

    class Meta:
        """
        Order the customer in ascending order based on time_slots
        """

        ordering = ['time_slots']


