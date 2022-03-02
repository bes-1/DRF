from rest_framework.viewsets import ModelViewSet
from usersapp.serializers import UserModelSerializer
from usersapp.models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
