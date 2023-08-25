from django.urls import path,include
from .views import *

urlpatterns = [
    path('',LoginAPI.as_view()),
]
