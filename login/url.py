from django.conf.urls import url
from registration import views

urlpatterns =[
    url('registration/', views.user_reg),
    url('view_customer/', views.cusview)
]
