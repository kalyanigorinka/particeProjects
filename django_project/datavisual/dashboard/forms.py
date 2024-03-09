from django import forms
from .models import OfficeData

class OfficeDataFrom(forms.ModelForm):
    class Meta:
        model = OfficeData
        fields = '__all__' 

# forms.py
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
