from django.urls import path
from . import views
from django.conf.urls.static import static # This allows us to serve our images imported from the model
from django.conf import settings  # This allows us to serve our images imported from the model

# Working  with url path
urlpatterns = [
    path("", views.vrequest)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
