
from django.urls import path

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions

@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def health(request):
    return Response({"status": "online"}, status=status.HTTP_200_OK)


urlpatterns = [
    path("health/", health, name="health")
]