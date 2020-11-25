from django import forms
from .models import Forms, Form
import re

SELECT_CHOICES = (
    ('Choose Project Type', 'Choose Project Type'),
    ('Single page', 'Single Page'),
    ('Multiple pages', 'Multiple Pages'),
    ('Custom Web App', 'Custom Web App'),
)


def check(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    regex2 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    return re.search(regex, email) or re.search(regex2, email)


class Message(forms.ModelForm):
    full_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'id': 'first_name'})

    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'id': 'user_mail', 'class': 'special'})
    )
    project_type = forms.ChoiceField(
        required=False,
        choices=SELECT_CHOICES,
        widget=forms.Select(attrs={'id': 'project_type', 'class': 'special'})
    )
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Message', 'id': 'message'}),
    )

    class Meta:
        model = Form
        fields = ['full_name', 'email', 'project_type', 'message']


