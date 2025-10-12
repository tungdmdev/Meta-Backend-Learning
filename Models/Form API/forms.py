from django import forms    

class ApplicationForm(forms.Form): 
    name = forms.CharField(label='Name of Applicant', max_length=50) 
    address = forms.CharField(label='Address', max_length=100) 
    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
    field = forms.ChoiceField(choices=posts)
    age = forms.IntegerField(min_value=20, max_value=60)
    price = forms.FloatField()
    upload = forms.FileField(upload_to ='uploads/')
    email = forms.EmailField(max_length = 254)
    gender = forms.CharField(max_length=1, choices=GENDER_CHOICES)
    