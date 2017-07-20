"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))



class ContactForm(forms.Form):
    first_name_Id = forms.CharField(max_length=200)
    last_name_Id = forms.CharField(max_length=200)
    email_Id = forms.EmailField(help_text='A valid email address, please.')
    MobileNo_Id = forms.IntegerField()
    contact_id = forms.IntegerField()



class UpdateForm(forms.Form):
    first_Id = forms.CharField(max_length=200)
    last_Id = forms.CharField(max_length=200)
    email = forms.EmailField(help_text='A valid email address, please.')
    Mobile_No = forms.IntegerField()


