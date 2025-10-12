from django.db import models
from django import forms
# Create your models here.
class Person(models.Model): 
    name = models.CharField(max_length=20) 
    email = models.EmailField() 
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)    

class Menu(models.Model):
    menu_item = models.CharField(max_length=200) 
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")


#QuerySet
class Customer(models.Model): 
    name = models.CharField(max_length=255) 

class Vehicle(models.Model): 
    name = models.CharField(max_length=255) 
    customer = models.ForeignKey( 
        Customer, 
        on_delete=models.CASCADE, 
        related_name='Vehicle' 
    ) 

#Form class
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)    