from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
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
    
    # Account creation fields
    create_account = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-checkbox',
            'id': 'id_create_account'
        }),
        label='Create an account to manage my reservations'
    )
    
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Create a password',
            'autocomplete': 'new-password',
            'id': 'id_password'
        }),
        label='Password'
    )
    
    password_confirm = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirm your password',
            'autocomplete': 'new-password',
            'id': 'id_password_confirm'
        }),
        label='Confirm Password'
    )
    
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

    def clean(self):
        cleaned_data = super().clean()
        create_account = cleaned_data.get('create_account')
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        email = cleaned_data.get('guest_email')
        
        if create_account:
            # Password is required if creating account
            if not password:
                self.add_error('password', 'Password is required to create an account.')
            elif len(password) < 8:
                self.add_error('password', 'Password must be at least 8 characters long.')
            
            if password and password != password_confirm:
                self.add_error('password_confirm', 'Passwords do not match.')
            
            # Check if email already exists as a user
            if email and User.objects.filter(email=email).exists():
                self.add_error('guest_email', 'An account with this email already exists. Please login instead.')
            
            # Validate password strength
            if password:
                try:
                    validate_password(password)
                except forms.ValidationError as e:
                    self.add_error('password', e.messages)
        
        return cleaned_data
