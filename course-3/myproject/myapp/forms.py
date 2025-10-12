from django import forms

from django.forms.widgets import NumberInput

class UserForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

class MyForm(forms.Form):
    name = forms.CharField(required=False, label='Your name', inital='Enter your name')
    age = forms.IntegerField(help_text='A valid age is required.')

class DemoForm(forms.Form):
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))