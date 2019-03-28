from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
]
