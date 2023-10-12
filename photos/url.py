from django.conf.urls import url
from photos import views

urlpatterns =[
    url('upload_photos/',views.up_photos),
    url('view_photos/',views.view_photos)
]
