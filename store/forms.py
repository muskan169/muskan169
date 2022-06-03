from django import forms
from django.contrib.auth.models import User

from .models.address import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ("user", "address", "city", "state", "zip_code")
