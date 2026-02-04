from django.shortcuts import render
from .models import Category, MenuItem


def menu_page(request):
    """Display the restaurant menu."""
    categories = Category.objects.prefetch_related('items').all()
    return render(request, 'menu/menu.html', {'categories': categories})
