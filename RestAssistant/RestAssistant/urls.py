from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gbarcode/', include('gbarcode.urls')),
    path('vdisplay/', include('vdisplay.urls')),
    path('vrequest/', include('vrequest.urls')),
]


