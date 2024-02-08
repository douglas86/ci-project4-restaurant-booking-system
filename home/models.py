from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Customer(models.Model):
    """
    Customer Model for storing data based on the user that is logged in
    """
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
        ordering = ['-created_at']
