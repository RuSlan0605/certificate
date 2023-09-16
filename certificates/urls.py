from django.urls import path
from .views import generate_pdf
from .views import imgpack

app_name = 'students'

urlpatterns = [
    path('', generate_pdf, name='generate'),
    path('draw/', imgpack, name='imagedraw'),
]
