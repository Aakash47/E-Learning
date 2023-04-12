from django import forms
from .models import ShippingAddress

class ShippingInfo(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ('address','city','state','zipcode')