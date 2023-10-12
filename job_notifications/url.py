from django.conf.urls import url
from job_notifications import views

urlpatterns =[
    url('post_jobnotifications/',views.jobntfcts),
    url('view_jobnotifications/',views.view_ntfctns),
    url('view_srjbntfs/',views.view_srjobntfctns)

]
