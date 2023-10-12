from django.conf.urls import url
from service_provider import views

urlpatterns =[
    url('add_service provider/',views.add_srvc_prvdr),
    url('view_service provider_profile/',views.srvc_prvdr_prfle),
    url('edit_service_provider_profile/(?P<idd>\w+)',views.sr_editprofile, name='edit'),
    # url('edit_service provider_profile/',views.sr_editprofile),

    url('view_sr/',views.sr_profile),
    url('view_service provider/',views.view_srvc_prvdr),
    url('sr_list/',views.sr_list),
    url('serv/', views.ser)
]
