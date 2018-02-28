from django.conf.urls import url
from .views import *


urlpatterns=[
    url(r'^register/$',Register.as_view()),
    url(r'^register_handle/$',Register.as_view()),
    url(r'^register_exist/$', register_exist),
    url(r'^login_handle/$', Login.as_view()),
    url(r'^login/$',Login.as_view()),
    url(r'^info/$', info),
    url(r'^order/', order),
    url(r'^site/$', site),
    url(r'^logout/$', logout),
    url(r'^user_center_order&(\d+)/$', user_center_order),
]