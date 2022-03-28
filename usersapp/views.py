from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from usersapp.serializers import UserModelSerializer
from usersapp.models import User
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import UpdateAPIView
from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions


# class UserLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 2


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    permission_classes = [DjangoModelPermissions]
    # pagination_class = UserLimitOffsetPagination
#
#
# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# def users_view(request, pk=None):
#     if pk:
#         user = get_object_or_404(User, pk=pk)
#         users = User.objects.filter(pk=user.pk)
#         serializer = UserModelSerializer(users, many=True)
#     else:
#         users = User.objects.all()
#         serializer = UserModelSerializer(users, many=True)
#     return Response(serializer.data)
#
#
# class UserUpdateAPIView(UpdateAPIView):
#     renderer_classes = [JSONRenderer]
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer


# class UserViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
#     serializer_class = UserModelSerializer
#     queryset = User.objects.all()
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     pagination_class = UserLimitOffsetPagination
