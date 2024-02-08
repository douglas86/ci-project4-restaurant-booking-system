from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class TableBookings(models.Model):
    """
    Table Bookings for when the customer wants to book at the restaurant
    """
    id = models.AutoField(primary_key=True)
    user_name = modles.ForeignKey(User, on_delete=models.CASCADE)
    seats = models.IntegerField()
    time_slots = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

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
