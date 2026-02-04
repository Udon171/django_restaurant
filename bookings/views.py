from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Table, Booking
from .forms import BookingForm


def booking_page(request):
    """Display the booking page with available tables."""
    tables = Table.objects.filter(is_active=True)
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been submitted!')
            return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(request, 'bookings/booking.html', {
        'tables': tables,
        'form': form,
    })


def booking_success(request):
    """Booking confirmation page."""
    return render(request, 'bookings/booking_success.html')


@login_required
def my_bookings(request):
    """View user's bookings."""
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})
