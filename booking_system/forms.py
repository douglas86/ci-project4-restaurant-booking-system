from django import forms
from django.contrib.auth.models import User


class UsernameResetPasswordForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)

    def clean_username(self):
        username = self.cleaned_data['username']

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('There is no user registered with this username.')
        return username

    def save(self, request, **kwargs):
        username = self.cleaned_data['username']
        user = User.objects.get(username=username)
        temporary_password = User.objects.make_random_password()
        user.set_password(temporary_password)
        user.save()
        # email = User.objects.get(username=username).email
        # self.cleaned_data['email'] = email
        return temporary_password
