from django.urls import path
from . import views

# Working  with url path
urlpatterns = [
    path("", views.vrequest)
]

