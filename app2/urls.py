from django.urls import path
from app2.views import *


app_name='baahu'


urlpatterns=[
    path('devasena/',devasena,name='devasena'),
    path('balah/',balah,name='balah'),
]