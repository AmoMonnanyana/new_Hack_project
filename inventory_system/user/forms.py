from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField()
    ROLE_CHOICES = (
        ('staff', 'Staff'),
        ('customer', 'Customer'),
        ('supplier', 'Supplier'),
        ('accountant', 'Accountant')
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'role', 'password1', 'password2']
