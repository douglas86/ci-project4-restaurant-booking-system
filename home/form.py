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

        # gets the value of the choice selected in a served model
        served_data_from_form = self.cleaned_data.get("served")

        # counts how many values are under the choice model served
        chef = ChefSpecial.objects.filter(served=served_data_from_form).count()

        # if there is more than 3 for the choice model served, then error occurs
        if chef >= 4:
            raise ValidationError("You have already have enough of that meal")
