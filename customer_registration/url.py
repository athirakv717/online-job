from django.conf.urls import url
from customer import views

urlpatterns =[
    url('view_customer/', views.view_cust)
]
