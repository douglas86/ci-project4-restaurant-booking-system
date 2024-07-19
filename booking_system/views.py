import datetime

from django.shortcuts import render
from django.views import View

from .forms import UsernameResetPasswordForm, ChangePasswordForm


class UsernamePasswordResetView(View):
    form_class = UsernameResetPasswordForm
    template_name = 'account/password_reset.html'

    # fetches current date of computer
    today = datetime.date.today()
    # fetches current hour based off the variable above
    current_hour = datetime.datetime.now().strftime("%H")
    # fetches current year based off the variable above
    year = today.year

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'year': self.year, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            temporary_password = form.save(request)
            return render(request, 'account/password_reset_done.html',
                          {'temporary_password': temporary_password})
        return render(request, self.template_name, {'form': form})


class ChangePasswordView(View):
    form_class = ChangePasswordForm
    template_name = 'account/password_change.html'

    # fetches current date of computer
    today = datetime.date.today()
    # fetches current hour based off the variable above
    current_hour = datetime.datetime.now().strftime("%H")
    # fetches current year based off the variable above
    year = today.year

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'year': self.year, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_password = form.save(request)
            user = authenticate(username=request.POST['username'], password=new_password)
            if user is not None:
                login(request, user)
            return redirect('account_login')
        return render(request, self.template_name, {'form': form})
