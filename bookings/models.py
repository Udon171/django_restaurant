from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.mail import send_mail
from django.conf import settings


class Table(models.Model):
    """Restaurant table that can be booked."""
    TABLE_TYPES = [
        ('standard', 'Standard (4 seats)'),
        ('large', 'Large Party (6+ seats)'),
    ]
    
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        help_text="Maximum number of guests"
    )
    table_type = models.CharField(max_length=20, choices=TABLE_TYPES, default='standard')
    is_active = models.BooleanField(default=True, help_text="Is this table available for booking?")

    class Meta:
        ordering = ['table_number']

    def __str__(self):
        return f"Table {self.table_number} ({self.get_table_type_display()})"


class Booking(models.Model):
    """A reservation made for a table."""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    # Guest details (no login required)
    guest_name = models.CharField(max_length=100, default='')
    guest_email = models.EmailField(default='')
    guest_phone = models.CharField(max_length=20, default='')
    
    # Optional user link for logged-in users
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='bookings',
        null=True,
        blank=True
    )
    
    # Booking details
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name='bookings',
        null=True,
        blank=True
    )
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Confirmation tracking
    confirmation_sent = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date', '-time']

    def __str__(self):
        return f"{self.guest_name} - {self.party_size} guests on {self.date} at {self.time}"
    
    def send_confirmation_email(self):
        """Send booking confirmation email to guest."""
        subject = f'Booking Confirmation - Django Restaurant'
        message = f"""
Dear {self.guest_name},

Thank you for your reservation at Django Restaurant!

Your Booking Details:
━━━━━━━━━━━━━━━━━━━━━
Date: {self.date.strftime('%A, %B %d, %Y')}
Time: {self.time.strftime('%I:%M %p')}
Party Size: {self.party_size} guests
Status: {self.get_status_display()}

{f'Special Requests: {self.special_requests}' if self.special_requests else ''}

We look forward to welcoming you!

Best regards,
Django Restaurant Team

━━━━━━━━━━━━━━━━━━━━━
If you need to modify or cancel your reservation, 
please visit your account dashboard or contact us.
        """
        
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@djangorestaurant.com',
                [self.guest_email],
                fail_silently=True,
            )
            self.confirmation_sent = True
            self.save(update_fields=['confirmation_sent'])
            return True
        except Exception:
            return False

    def send_update_email(self):
        """Send booking update confirmation email."""
        subject = 'Reservation Updated - Django Restaurant'
        message = f"""
Dear {self.guest_name},

Your reservation at Django Restaurant has been updated.

Updated Booking Details:
━━━━━━━━━━━━━━━━━━━━━
Date: {self.date.strftime('%A, %B %d, %Y')}
Time: {self.time.strftime('%I:%M %p')}
Party Size: {self.party_size} guests
Status: {self.get_status_display()}

{f'Special Requests: {self.special_requests}' if self.special_requests else ''}

We look forward to welcoming you!

Best regards,
Django Restaurant Team
        """
        
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@djangorestaurant.com',
                [self.guest_email],
                fail_silently=True,
            )
            return True
        except Exception:
            return False

    def send_cancellation_email(self):
        """Send booking cancellation confirmation email."""
        subject = 'Reservation Cancelled - Django Restaurant'
        message = f"""
Dear {self.guest_name},

Your reservation at Django Restaurant has been cancelled.

Cancelled Booking Details:
━━━━━━━━━━━━━━━━━━━━━
Date: {self.date.strftime('%A, %B %d, %Y')}
Time: {self.time.strftime('%I:%M %p')}
Party Size: {self.party_size} guests

We're sorry to see you go! If you'd like to make a new reservation,
please visit our website anytime.

Best regards,
Django Restaurant Team
        """
        
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@djangorestaurant.com',
                [self.guest_email],
                fail_silently=True,
            )
            return True
        except Exception:
            return False
