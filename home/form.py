from django import forms
from django.core.exceptions import ValidationError

from .models import ChefSpecial


class ChefForm(forms.ModelForm):
    """
    Form for ChefSpecial model
    """

    def clean(self):
        """
        This method is used to validate how many records are in the Chefs model
        :return:
        """

        # Stops the storing of more than 9 records in the ChefSpecial model
        total_records = ChefSpecial.objects.all().count()
        if total_records > 9:
            raise ValidationError('DB limit reached for more than 2')

        # checks how many records are stored from breakfast, lunch and supper
        # stops storing of more than 3 records per meal time
        for i in range(3):
            chef = ChefSpecial.objects.filter(served=i).count()
            if chef >= 3:
                raise ValidationError("You already have enough of that particular meal")
