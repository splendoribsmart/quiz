"""
URL configuration for quiz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from game import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('main-phone/', views.main_phone_view, name='mainphone'),
    path('main-desktop/', views.main_desktop_view, name='maindesktop'),

    # Authentication URLs
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('logout/', views.custom_logout, name='custom_logout'),
    path('logout-phone/', views.custom_logout, name='logoutphone'),
    path('logout-desktop/', views.custom_logout, name='logoutdesktop'),
    # path('accounts/register/', RegisterView.as_view(), name='register'),  # Replace 'RegisterView' with your actual registration view

    path('game/', include("game.urls")),
    path('', include("autheticate.urls")),
    path('accounts/', include('allauth.urls')),
    path('countdown/', include('countdown_timer.urls')),
    
    path('get_remaining_time/', views.get_remaining_time, name='get_remaining_time'),
    path('get_remaining_time_1/', views.get_remaining_time_1, name='get_remaining_time_1'),
    path('get_elapsed_time/', views.get_elapsed_time, name='get_elapsed_time'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)