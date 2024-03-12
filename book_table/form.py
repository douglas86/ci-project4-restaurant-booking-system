from django import forms

from .models import TableBookings


class BookTableForm(forms.ModelForm):
    """
    Form for booking a table
    """

    class Meta:
        model = TableBookings
        fields = ['seats', 'time_slots', ]
        widgets = {'time_slots': forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})}
        labels = {'seats': 'Number of seats', 'time_slots': 'time slots'}
