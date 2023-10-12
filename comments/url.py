from django.conf.urls import url
from comments import views

urlpatterns = [
    url('comments/',views.comnt),
    url('view_commnt/',views.view_cmmnts)
]

