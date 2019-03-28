from django.contrib import admin
from django.urls import path, include

from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('book.urls')),

    # path('users/', include('users.urls')),
    # path('users/', include('django.contrib.auth.urls')),
]
