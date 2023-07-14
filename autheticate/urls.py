from django.urls import path
from .views import register, user_login
from .views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete, password_change, password_change_done


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
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