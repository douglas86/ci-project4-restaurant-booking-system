import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView, CreateView, DeleteView, UpdateView

from .form import BookTableForm
from .models import Customer


# create
class BookTableCreateView(LoginRequiredMixin, CreateView):
    """
    This view is used to write data to the database
    """

    # model to be used
    model = Customer
    # form to be used called from form.py
    form_class = BookTableForm
    # when form is valid send a success message
    message = "You have successfully booked your table"

    time_slot = ''

    def get_queryset(self):
        """
        Built in method normally used to gather data from the database
        :return:
        """

        # variable to fetch time_slot only by date
        format_time_slot = self.time_slot.split('T')[0]
        # variable to fetch data from a Customer model by user
        # only returns its value
        query = Customer.objects.filter(user=self.request.user).values()

        # iterate over query from database
        for items in query:
            # iterate over items with key, value pairs
            for key, value in items.items():
                # check the time_slot from a database
                if key == 'time_slots':
                    # check to see if the date has been used already
                    if str(value.date()) == format_time_slot:
                        # if that date has not been used, then return False
                        return False

        # if that date has not been used, then return True
        return True

    def get_success_url(self):
        """
        Built in method normally runs on form validation success
        :return:
        """

        # send a success message to template
        messages.success(self.request, self.message)
        return reverse('book_table:table')

    def form_valid(self, form):
        """
        Built in method normally used to validate the form
        :param form:
        :return:
        """

        self.time_slot = form['time_slots'].value()

        # form validation check
        if self.get_queryset():
            # save form only if there is no booking for the current day
            # based on logged-in user
            instance = form.save(commit=False)
            instance.user = self.request.user
        else:
            # return error message if there is already an entry in db
            self.message = 'You have already booked please choose anther day'
            messages.error(self.request, self.message)
            return redirect('book_table:table')
        return super().form_valid(form)


# read
class BookTableView(LoginRequiredMixin, TemplateView, FormView):
    """
    This view is used to read and render data from database to template
    """

    # template to send data to
    template_name = 'book_table/table.html'
    # form to be used called from form.py
    form_class = BookTableForm
    # this will only send paginate_by number to template at once
    paginate_by = 10

    # fetches current date of computer
    today = datetime.date.today()
    # fetches current hour based off the variable above
    current_hour = datetime.datetime.now().strftime("%H")
    # fetches current year based off the variable above
    year = today.year

    def format_time_stamps_for_display(self):
        """
        This method is used to format time stamps to day month year time
        :return: properly formatted time stamps from queryset as a list
        """

        # list to return properly formatted time stamps
        data = []

        # for loop to iterate over fetch data variable
        for item in self.get_data().values():
            # dictionary to keep track of properly
            # formatted data from queryset
            data_item = {}
            # for loop to iterate over items in queryset
            for key, value in item.items():
                try:
                    # format all time stamps to day, month, year and time
                    data_item[key] = value.strftime('%d %B %Y %H:%M')
                except AttributeError:
                    # if no time stamp on data leave as is
                    data_item[key] = value

            # once key, value loop is complete
            # push data to an item list for template
            data.append(data_item)

        return data

    def get_data(self):
        """
        Fetch data from a database by order in ascending order by time_slots
        :return:
        """

        return Customer.objects.filter(user=self.request.user).order_by('-time_slots')

    def get_queryset(self):
        """
        Built in method used to gather data for get_context_data method
        :return:
        """

        # variable to run helper function
        # for formatting time stamps
        data = self.format_time_stamps_for_display()

        return data

    def get_context_data(self, **kwargs):
        """
        Built in method used to render data to template
        :param kwargs:
        :return:
        """

        # context variable for storing all kwargs
        # this variable makes it easier to send to template
        context = super(BookTableView, self).get_context_data(**kwargs)

        # context for all data stored in Customer model
        context['customer'] = self.get_queryset()
        # context for displaying last entry in customer context
        context['last_booking'] = context['customer']

        return {"year": self.year, 'form': self.form_class(), 'context': context}


# update
class BookTableUpdateView(LoginRequiredMixin, UpdateView):
    """
    This view is used to update a record from the booking table database
    """

    template_name = 'book_table/table.html'
    model = Customer
    form_class = BookTableForm
    success_url = "/table"


# delete
class BookTableDeleteView(LoginRequiredMixin, DeleteView):
    """
    This view is used to delete a record from the booking table database
    """

    template_name = 'book_table/table.html'
    model = Customer
    success_url = "/table"
