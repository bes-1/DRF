from rest_framework.serializers import ModelSerializer, StringRelatedField, HyperlinkedRelatedField, SlugRelatedField
from notesapp.models import Project, ToDo
from usersapp.models import User
from usersapp.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    # user_set = UserModelSerializer(many=True)


    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    # user = StringRelatedField()
    # project = StringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'

#
# class ToDoModelSerializer(ModelSerializer):
#     ToDo.__name = ProjectModelSerializer()
#
#     class Meta:
#         model = ToDo
#         fields = '__all__'
