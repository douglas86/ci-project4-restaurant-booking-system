from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView, CreateView

from .form import BookTableForm
from .models import Customer


class BookTableCreateView(LoginRequiredMixin, CreateView):
    """
    This view is used to write data to the database
    """

    # model to be used
    model = Customer
    # form to be used called from form.py
    form_class = BookTableForm
    # when form is valid send a success message
    success_message = "You have successfully booked your table"

    def get_queryset(self):
        """
        Built in method normally used to gather data from the database
        :return:
        """

        # counts how many records are in db based on user
        queryset = Customer.objects.filter(user=self.request.user).count()

        return queryset

    def get_success_url(self):
        """
        Built in method normally runs on form validation success
        :return:
        """

        # send a success message to template
        messages.success(self.request, self.success_message)
        return reverse('book_table:table')

    def form_valid(self, form):
        """
        Built in method normally used to validate the form
        :param form:
        :return:
        """

        # form validation check
        if self.get_queryset() <= 0:
            # save form only if there is no booking for the current day
            # based on logged-in user
            instance = form.save(commit=False)
            instance.user = self.request.user
        else:
            # return error message if there is already an entry in db
            self.success_message = 'You have already booked please choose anther day'
            messages.error(self.request, self.success_message)
            return redirect('book_table:table')
        return super().form_valid(form)


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
        context['last_booking'] = context['customer'][0]

        return {'form': self.form_class(), 'context': context}
