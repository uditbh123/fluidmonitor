from django import forms
from .models import Reading

class ReadingForm(forms.ModelForm):
    class Meta:
        model = Reading
        fields = ['sensor_name', 'value', 'unit', 'notes']
        widgets = {
            'sensor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }