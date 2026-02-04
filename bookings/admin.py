from django.contrib import admin
from .models import Table, Booking


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_active')
    list_filter = ('is_active', 'capacity')
    search_fields = ('table_number',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'time', 'party_size', 'status', 'created_at')
    list_filter = ('status', 'date', 'table')
    search_fields = ('user__username', 'user__email')
    date_hierarchy = 'date'
    ordering = ['-date', '-time']
