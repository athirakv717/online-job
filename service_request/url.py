from django.conf.urls import url
from service_request import views
urlpatterns =[
    url('post_service request/', views.post_srvc_reqst),
    url('view_service request_actns/', views.srvc_reqst_actns),
    url('view_service request/', views.view_srvc_reqst)
    ]