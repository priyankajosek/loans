from django.urls import path
from .views import EmiView

urlpatterns = [
    path('emi/',EmiView.as_view()),
    ]
