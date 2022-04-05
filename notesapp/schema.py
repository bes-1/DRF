import graphene
from graphene_django import DjangoObjectType
from notesapp.models import ToDo, Project
from usersapp.models import User


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):
    all_todo = graphene.List(ToDoType)

    def resolve_all_todo(root, info):
        return ToDo.objects.all()

    all_project = graphene.List(ProjectType)

    def resolve_all_project(root, info):
        return Project.objects.all()

    all_user = graphene.List(UserType)

    def resolve_all_user(root, info):
        return User.objects.all()

    todo_by_id = graphene.Field(ToDoType, pk=graphene.Int(required=True))

    def resolve_todo_by_id(root, info, pk):
        try:
            return ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            return None


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, email):
        user = User(first_name=first_name, last_name=last_name, email=email)
        user.save()
        return cls(user)


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        email = graphene.String(required=False)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, id, first_name=None, last_name=None, email=None):
        user = User.objects.get(pk=id)
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
        if first_name or last_name or email:
            user.save()
        return cls(user)


class Mutations(graphene.ObjectType):
    create_user = UserCreateMutation.Field()
    update_user = UserUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
