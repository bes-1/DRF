from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, \
    DestroyModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from notesapp.serializers import ProjectModelSerializer, ToDoModelSerializer
from notesapp.models import Project, ToDo
from rest_framework.pagination import LimitOffsetPagination


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin,
                     GenericViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    pagination_class = ProjectLimitOffsetPagination

    def get_queryset(self):
        queryset = Project.objects.all()
        part_name = self.request.query_params.get('part_name')
        if part_name:
            return queryset.filter(name__contains=part_name)
        return queryset


class ToDoViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin,
                  GenericViewSet):
    serializer_class = ToDoModelSerializer
    queryset = ToDo.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    pagination_class = ToDoLimitOffsetPagination
    filterset_fields = ['project']

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_active = False
        todo.save()
        return Response(status=status.HTTP_200_OK)
