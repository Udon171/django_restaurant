from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
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
        create_account = form.cleaned_data.get('create_account')
        password = form.cleaned_data.get('password')
        
        # Create user account if requested
        if create_account and password:
            try:
                # Create user with email as username
                user = User.objects.create_user(
                    username=booking.guest_email,
                    email=booking.guest_email,
                    password=password,
                    first_name=booking.guest_name.split()[0] if booking.guest_name else '',
                    last_name=' '.join(booking.guest_name.split()[1:]) if len(booking.guest_name.split()) > 1 else ''
                )
                booking.user = user
                # Log the user in
                login(request, user)
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'errors': {'guest_email': ['Could not create account. Please try again.']}
                }, status=400)
        elif request.user.is_authenticated:
            # Link to existing logged-in user
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
        
        response_data = {
            'success': True,
            'booking': {
                'name': booking.guest_name,
                'date': booking.date.strftime('%A, %B %d, %Y'),
                'time': booking.time.strftime('%I:%M %p'),
                'party_size': booking.party_size,
                'email': booking.guest_email,
            }
        }
        
        # Include account creation status
        if create_account and password:
            response_data['account_created'] = True
            
        return JsonResponse(response_data)
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
    bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})


@login_required
def edit_booking(request, booking_id):
    """Edit an existing booking."""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        # Get the updated values
        new_date = request.POST.get('date')
        new_time = request.POST.get('time')
        new_party_size = request.POST.get('party_size')
        new_special_requests = request.POST.get('special_requests', '')
        
        # Update booking
        if new_date:
            booking.date = new_date
        if new_time:
            booking.time = new_time
        if new_party_size:
            booking.party_size = int(new_party_size)
            # Reassign table if party size changed significantly
            if booking.party_size > 4:
                available_table = Table.objects.filter(
                    table_type='large',
                    is_active=True
                ).first()
            else:
                available_table = Table.objects.filter(
                    table_type='standard',
                    is_active=True
                ).first()
            booking.table = available_table
        
        booking.special_requests = new_special_requests
        booking.save()
        
        # Send update confirmation email
        booking.send_update_email()
        
        messages.success(request, 'Your reservation has been updated successfully!')
        return redirect('my_bookings')
    
    # GET request - show edit form
    from .forms import BookingForm
    time_choices = BookingForm.TIME_CHOICES
    return render(request, 'bookings/edit_booking.html', {
        'booking': booking,
        'time_choices': time_choices
    })


@login_required
@require_POST
def cancel_booking(request, booking_id):
    """Cancel a booking."""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.status = 'cancelled'
    booking.save()
    
    # Send cancellation email
    booking.send_cancellation_email()
    
    messages.success(request, 'Your reservation has been cancelled.')
    return redirect('my_bookings')
