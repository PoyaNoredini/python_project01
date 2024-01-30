from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    # phone_number = forms.CharField(max_length=11, required=True)
    GENDER_CHOICES = [
        ("woman", "Woman"),
        ("man", "Man"),
    ]
    name = forms.CharField(max_length=25, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    address = forms.CharField(max_length=250, widget=forms.Textarea)

