from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from home import views as index_views
from about import views as about_views
from bookings import views as booking_views
from menu import views as menu_views

urlpatterns = [
    path('', index_views.index, name='index'),
    path('about/', about_views.about_me, name='about'),
    path('admin/', admin.site.urls),
    path('book/', booking_views.booking_page, name='booking'),
    path('book/submit/', booking_views.submit_booking, name='submit_booking'),
    path('book/success/', booking_views.booking_success, name='booking_success'),
    path('book/my-bookings/', booking_views.my_bookings, name='my_bookings'),
    path('menu/', menu_views.menu_page, name='menu'),
    # Auth URLs
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
