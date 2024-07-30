# salesapp/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),  # Add logout URL
    path('accounts/', include('django.contrib.auth.urls')),  # Include auth URLs if needed
    path('sales/', include('sales.urls')),  # Include sales app URLs
    # Add more paths for other apps if needed
]
