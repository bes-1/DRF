from rest_framework.viewsets import ModelViewSet
from notesapp.serializers import ProjectModelSerializer, ToDoModelSerializer
from notesapp.models import Project, ToDo


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoModelSerializer
    queryset = ToDo.objects.all()
