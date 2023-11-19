from django.urls import path
from .views import *

urlpatterns = [
    path('', UploadImageView.as_view(), name='upload-image'),
    # Add more URL patterns as needed for your API views
]