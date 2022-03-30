"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from notesapp.views import ProjectViewSet, ToDoViewSet
from usersapp.views import UserModelViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('project', ProjectViewSet, basename='project')
router.register('todo', ToDoViewSet)
# filter_router = DefaultRouter()
# filter_router.register('param', UserParamFilterViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Users",
        default_version='1.0',
        description="Documentation to out project",
        contact=openapi.Contact(email="test@gb.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(AllowAny, )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/userss/v1/', include('usersapp.urls', namespace='1.0')),
    # в пути написал userss (два раза s), так как router перехватывает.
    path('api/userss/v2/', include('usersapp.urls', namespace='2.0')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', obtain_auth_token),
    path('swagger/', schema_view.with_ui()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),
    # path('views/', users_view),
    # path('views/<int:pk>/', users_view),
    # path('update_user/<int:pk>/', UserUpdateAPIView.as_view()),
]
