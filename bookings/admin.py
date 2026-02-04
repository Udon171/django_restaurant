from django.contrib import admin
from .models import Table, Booking


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'table_type', 'is_active')
    list_filter = ('is_active', 'capacity', 'table_type')
    search_fields = ('table_number',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'guest_email', 'guest_phone', 'table', 'date', 'time', 'party_size', 'status', 'confirmation_sent', 'created_at')
    list_filter = ('status', 'date', 'table', 'confirmation_sent')
    search_fields = ('guest_name', 'guest_email', 'guest_phone')
    date_hierarchy = 'date'
    ordering = ['-date', '-time']
    readonly_fields = ('created_at', 'updated_at', 'confirmation_sent')
