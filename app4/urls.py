from django.urls import path
from app4.views import factorial_view

urlpatterns = [
    path('factorial_view', factorial_view),
]