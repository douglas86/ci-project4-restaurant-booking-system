from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class UsernameResetPasswordForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)

    def save(self, request):
        username = self.cleaned_data['username']

        try:
            user = User.objects.get(username=username)
            temporary_password = User.objects.make_random_password()
            user.set_password(temporary_password)
            user.save()
            return temporary_password
        except User.DoesNotExist:
            raise forms.ValidationError('Username does not exist')


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ChangePasswordForm, self).__init__(user, *args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data['old_password']

        if not self.user.check_password(old_password):
            raise forms.ValidationError('Incorrect old password')
        return old_password
