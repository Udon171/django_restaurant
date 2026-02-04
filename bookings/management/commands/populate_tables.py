from django.core.management.base import BaseCommand
from bookings.models import Table


class Command(BaseCommand):
    help = 'Populates the database with 55 restaurant tables'

    def handle(self, *args, **options):
        # Clear existing tables
        Table.objects.all().delete()
        self.stdout.write('Cleared existing tables...')
        
        tables_created = 0
        
        # Create 50 standard tables (4 seats each)
        for i in range(1, 51):
            Table.objects.create(
                table_number=i,
                capacity=4,
                table_type='standard',
                is_active=True
            )
            tables_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created 50 standard tables (4 seats each)'))
        
        # Create 5 large party tables (6-12 seats)
        # Tables 51-55 are reserved for large parties
        large_capacities = [6, 8, 8, 10, 12]  # Varying capacities for large parties
        for i, capacity in enumerate(large_capacities, start=51):
            Table.objects.create(
                table_number=i,
                capacity=capacity,
                table_type='large',
                is_active=True
            )
            tables_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created 5 large party tables (6-12 seats)'))
        self.stdout.write(self.style.SUCCESS(f'\n✓ Total: {tables_created} tables created successfully!'))
        
        # Summary
        self.stdout.write('\n--- Table Summary ---')
        self.stdout.write(f'Standard tables (1-50): 50 tables, 4 seats each')
        self.stdout.write(f'Large party tables (51-55): 5 tables, 6-12 seats')
        self.stdout.write(f'Total seating capacity: {50*4 + sum(large_capacities)} guests')
