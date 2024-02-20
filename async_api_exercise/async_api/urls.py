from django.urls import path
from .views import retrieve_data

urlpatterns = [
    path('retrieve_data/', retrieve_data, name='fetch_data'),
]
