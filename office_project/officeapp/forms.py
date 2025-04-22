from django import forms 
from .models import Office

class OfficeForm(forms.ModelForm): 
    class Meta:
        model = Office 
        fields = ['name', 'location', 'employees_count']


 
