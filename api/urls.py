from django.conf.urls import url

from api.views.auth import device_auth_view
from api.views.auth import member_auth_view
from api.views.profile import get_profile_data_view

urlpatterns = [
    url(r'^device\-auth/(\w+)/(\w+)/', device_auth_view, name='api_device_auth'),
    url(r'^member\-auth/(\w+)/(.+)/', member_auth_view, name='api_member_auth'),

    url(r'^get\-profile\-data/(\w+)/(\w+)/', get_profile_data_view, name='api_get_profile_data'),
]
