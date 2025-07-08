from django import forms
from .models import Patient, Intervention, Procedure



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "last_name", "email", "age"]