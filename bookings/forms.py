from django import forms
from .models import Booking, Table


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'party_size', 'special_requests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-input'}),
            'table': forms.Select(attrs={'class': 'form-input'}),
            'party_size': forms.NumberInput(attrs={'class': 'form-input', 'min': 1, 'max': 12}),
            'special_requests': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table'].queryset = Table.objects.filter(is_active=True)
        self.fields['special_requests'].required = False
