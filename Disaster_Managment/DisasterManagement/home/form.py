from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signupform(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    address1 = forms.CharField(max_length=50)
    address2 = forms.CharField(max_length=50)
    pincode = forms.CharField(max_length=6)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)

    class meta:
        model = User
        fields = (
            'Username', 'password', 'password2', 'email', 'first_name', 'last_name', 'address1', 'address2', 'pincode',
            'state', 'city')

    def save(self, commit=True):
        user = super(signupform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.address1 = self.cleaned_data['address1']
        user.address2 = self.cleaned_data['address2']
        user.city = self.cleaned_data['city']
        user.state = self.cleaned_data['state']

        if commit:
            user.save()
        return user
