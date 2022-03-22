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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from notesapp.views import ProjectViewSet, ToDoViewSet
from usersapp.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('project', ProjectViewSet, basename='project')
router.register('todo', ToDoViewSet)
# filter_router = DefaultRouter()
# filter_router.register('param', UserParamFilterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('views/', users_view),
    # path('views/<int:pk>/', users_view),
    # path('update_user/<int:pk>/', UserUpdateAPIView.as_view()),
]
