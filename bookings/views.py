from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Table, Booking
from .forms import BookingForm
import json


def booking_page(request):
    """Display the booking page."""
    form = BookingForm()
    return render(request, 'bookings/booking.html', {'form': form})


@require_POST
def submit_booking(request):
    """Handle booking form submission via AJAX."""
    form = BookingForm(request.POST)
    
    if form.is_valid():
        booking = form.save(commit=False)
        
        # Link to user if logged in
        if request.user.is_authenticated:
            booking.user = request.user
        
        # Auto-assign a table based on party size
        party_size = booking.party_size
        if party_size > 4:
            # Large party - use reserved tables
            available_table = Table.objects.filter(
                table_type='large',
                is_active=True
            ).first()
        else:
            # Standard party
            available_table = Table.objects.filter(
                table_type='standard',
                is_active=True
            ).first()
        
        booking.table = available_table
        booking.status = 'confirmed'
        booking.save()
        
        # Send confirmation email
        booking.send_confirmation_email()
        
        return JsonResponse({
            'success': True,
            'booking': {
                'name': booking.guest_name,
                'date': booking.date.strftime('%A, %B %d, %Y'),
                'time': booking.time.strftime('%I:%M %p'),
                'party_size': booking.party_size,
                'email': booking.guest_email,
            }
        })
    else:
        return JsonResponse({
            'success': False,
            'errors': form.errors
        }, status=400)


def booking_success(request):
    """Booking confirmation page."""
    return render(request, 'bookings/booking_success.html')


@login_required
def my_bookings(request):
    """View user's bookings."""
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})
