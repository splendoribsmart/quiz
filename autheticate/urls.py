from django.urls import path
from .views import register_desktop, register_phone, user_login_desktop, user_login_phone
from .views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete, password_change, password_change_done


urlpatterns = [
    path('register-desktop/', register_desktop, name='registerdesktop'),
    path('register-phone/', register_phone, name='registerphone'),
    path('login-desktop/', user_login_desktop, name='logindesktop'),
    path('login-phone/', user_login_phone, name='loginphone'),
    # Other URL patterns

    # Password Management
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset/done/', password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', password_reset_complete, name='password_reset_complete'),
    
    # Other URL patterns
    path('password_change/', password_change, name='password_change'),
    path('password_change/done/', password_change_done, name='password_change_done'),
]