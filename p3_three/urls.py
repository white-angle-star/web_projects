from django.urls import path
from p3_three.views import *

urlpatterns = [
    path('', page_3.as_view(), name='page_3'),
]
