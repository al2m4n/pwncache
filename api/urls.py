from django.urls import path
from .views import retrieve_asset

urlpatterns = [
    path("<str:contract_address>/<str:token_id>/", retrieve_asset),
]
