import datetime

from django import forms

from .models import Customer


class BookTableForm(forms.ModelForm):
    """
    Form for booking a table
    """

    class Meta:
        """
        Metaclass is a built-in method to give added functionality to forms
        """

        model = Customer
        fields = ['seats', 'time_slots', ]
        widgets = {'time_slots': forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})}
        labels = {'seats': 'Number of seats', 'time_slots': 'time slots'}

    def __init__(self, *args, **kwargs):
        """
        Initializes this class with required fields
        :param args:
        :param kwargs:
        """

        super(BookTableForm, self).__init__(*args, **kwargs)

        # sets validation for seat field
        self.fields['seats'].required = True
        self.fields['seats'].widget.attrs['min'] = 1
        self.fields['seats'].widget.attrs['max'] = 10

        # sets validation for time_slots field
        self.fields['time_slots'].required = True
        # this sets a validation to enter a date more than 1 hour from now
        self.fields['time_slots'].widget.attrs['min'] = (
                datetime.datetime.now() + datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M')
