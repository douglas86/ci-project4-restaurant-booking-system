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


class ChangePasswordForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', max_length=150)
    old_password = forms.CharField(label='Old Password', max_length=150)

    def clean_username(self):
        username = self.cleaned_data['username']

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('There is no user registered with this username.')
        return username

    def clean_old_password(self):
        old_password = self.cleaned_data['old_password']

        if not User.objects.filter(username=old_password).exists():
            raise forms.ValidationError('There is no old password registered with this username.')
        return old_password

    def save(self, request, **kwargs):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        return user
