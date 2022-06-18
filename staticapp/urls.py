from django.urls import path
from staticapp.views import home

urlpatterns = [
    path('', home, name='home'),
]
