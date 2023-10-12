from django.conf.urls import url
from notifications import views

urlpatterns =[
    url('notifications/',views.ntfcts),
    url('view_notfctns/',views.view_ntfctns),
    url('view_srntfs/',views.view_srntfs)
]
