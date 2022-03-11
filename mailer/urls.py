from django.urls import URLPattern, path
from .views import sendMail

urlpatterns = [
    path('', sendMail),
]
