from django import forms

from .models import Customer


class BookTableForm(forms.ModelForm):
    """
    Form for booking a table
    """

    class Meta:
        model = Customer
        fields = ['seats', 'time_slots', ]
        widgets = {'time_slots': forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})}
        labels = {'seats': 'Number of seats', 'time_slots': 'time slots'}
