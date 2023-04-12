from django import forms
from . models import Fcontact

class FcontactForm(forms.ModelForm):
    class Meta:
        model = Fcontact
        fields = ('description', 'budget', 'contact_no')