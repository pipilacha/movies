"""
URL configuration for moviesapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions

@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def health(request):
    return Response({"status": "online"}, status=status.HTTP_200_OK)

urlpatterns = [
    path("health/", health, name="health"),
    path('movies/', include('movies.urls')),
    path('admin/', admin.site.urls),
]
