from django.shortcuts import render


def about_me(request):
    """Display the about page with contact info and social feed."""
    return render(request, 'about/about.html')