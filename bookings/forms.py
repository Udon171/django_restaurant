from django import forms
from .models import Booking
from datetime import date, time


class BookingForm(forms.ModelForm):
    TIME_CHOICES = [
        ('12:00', '12:00 PM'),
        ('12:30', '12:30 PM'),
        ('13:00', '1:00 PM'),
        ('13:30', '1:30 PM'),
        ('14:00', '2:00 PM'),
        ('14:30', '2:30 PM'),
        ('15:00', '3:00 PM'),
        ('17:00', '5:00 PM'),
        ('17:30', '5:30 PM'),
        ('18:00', '6:00 PM'),
        ('18:30', '6:30 PM'),
        ('19:00', '7:00 PM'),
        ('19:30', '7:30 PM'),
        ('20:00', '8:00 PM'),
        ('20:30', '8:30 PM'),
        ('21:00', '9:00 PM'),
    ]
    
    time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(attrs={'class': 'form-input'}))
    
    class Meta:
        model = Booking
        fields = ['guest_name', 'guest_email', 'guest_phone', 'date', 'time', 'party_size', 'special_requests']
        widgets = {
            'guest_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your full name',
                'required': True
            }),
            'guest_email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'your@email.com',
                'required': True
            }),
            'guest_phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+44 7XXX XXXXXX',
                'required': True
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input',
                'min': date.today().isoformat()
            }),
            'party_size': forms.NumberInput(attrs={
                'class': 'form-input',
                'min': 1,
                'max': 12,
                'value': 2
            }),
            'special_requests': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 3,
                'placeholder': 'Any dietary requirements or special requests?'
            }),
        }
        labels = {
            'guest_name': 'Full Name',
            'guest_email': 'Email Address',
            'guest_phone': 'Phone Number',
            'party_size': 'Number of Guests',
            'special_requests': 'Special Requests (optional)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['special_requests'].required = False
