from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Table(models.Model):
    """Restaurant table that can be booked."""
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        help_text="Maximum number of guests"
    )
    is_active = models.BooleanField(default=True, help_text="Is this table available for booking?")

    class Meta:
        ordering = ['table_number']

    def __str__(self):
        return f"Table {self.table_number} (seats {self.capacity})"


class Booking(models.Model):
    """A reservation made by a user for a specific table."""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name='bookings'
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

    class Meta:
        ordering = ['-date', '-time']
        # Prevent double-booking: one table can only have one booking per date/time
        constraints = [
            models.UniqueConstraint(
                fields=['table', 'date', 'time'],
                name='unique_booking_slot'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - Table {self.table.table_number} on {self.date} at {self.time}"
