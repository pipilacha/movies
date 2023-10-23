from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework import status

from .serializers import ActorSerializer
from .models import Actor
from moviesapp.base_responses import SuccessResponse, ErrorResponse

# Create your views here.

class ActorViewSet(ViewSet):
    '''
    Create, List, Rettrieve, Update, Delete actor/s
    '''

    def list(self, request):
        queryset = Actor.objects.all()
        serializer = ActorSerializer(queryset, many=True, context={'request': request})
        return SuccessResponse(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = ActorSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data, status=status.HTTP_201_CREATED)
        if serializer.errors['name'][0].code == 'unique':
            return ErrorResponse(serializer.errors, status=status.HTTP_409_CONFLICT)
        return ErrorResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        # queryset = Actor.objects.all()
        # actor = get_object_or_404(queryset, pk=pk) # automatically raises HTTP404
        try:
            actor = Actor.objects.get(pk=pk)
            serializer = ActorSerializer(actor, context={'request': request})
            return SuccessResponse(serializer.data, status=status.HTTP_200_OK)
        except Actor.DoesNotExist:
            return ErrorResponse({
                'detail': 'Actor does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, pk=None):
        try:
            actor = Actor.objects.get(pk=pk)
            db_seralizer = ActorSerializer(actor, context={'request': request})
            body_serializer = ActorSerializer(data=request.data, context={'request': request})

            if body_serializer.is_valid():
                db_seralizer.update(actor, body_serializer.validated_data)
                return SuccessResponse(db_seralizer.data, status=status.HTTP_200_OK)
            
            if body_serializer.errors['name'][0].code == 'unique':
                return ErrorResponse(body_serializer.errors, status=status.HTTP_409_CONFLICT)
            
            return ErrorResponse(body_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Actor.DoesNotExist:
            return ErrorResponse({
                'detail': 'Actor does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, pk=None):
        try:
            Actor.objects.get(pk=pk).delete()
            return SuccessResponse(status=status.HTTP_204_NO_CONTENT)
        except Actor.DoesNotExist:
            return ErrorResponse({
                'detail': 'Actor does not exist'
            }, status=status.HTTP_404_NOT_FOUND)