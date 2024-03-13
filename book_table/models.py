import uuid

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Customer(models.Model):
    """
    Table Bookings for when the customer wants to book at the restaurant
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
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
        return self.user_name

    class Meta:
        """
        Order the customer in ascending order based on time_slots
        """
        ordering = ['time_slots']


class Voucher(models.Model):
    """
    Vouchers for when the customer wants to book a table at the restaurant
    vouchers are automatically applied to the booking
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        I want to display data based on the title of the voucher
        :return:
        """
        return self.title

    class Meta:
        """
        Order the customer in ascending by created_at date
        """
        ordering = ['created_at']
