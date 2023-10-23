from rest_framework.serializers import HyperlinkedModelSerializer

from actors.models import Actor


class ActorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ['url', 'id', 'name', 'created_at', 'updated_at']

