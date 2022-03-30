from django.urls import path
from usersapp.views import UserModelViewSet

app_name = 'userapp'

urlpatterns = [
    path('', UserModelViewSet.as_view({'get': 'list'}))
]