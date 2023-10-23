from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from actors.serializers import ActorSerializer

from actors.models import Actor


class ActorEndpointsTests(APITestCase):

    def test_create_actor(self):
        '''
        Test we can create an actor
        '''
        url = reverse('actor-list')
        actor = {'name': 'John Savage'}
        response = self.client.post(url, actor, format='json')
        self.assertContains(response=response, text=actor['name'], count=1, status_code=status.HTTP_201_CREATED)
        self.assertEquals(Actor.objects.count(), 1)
        self.assertEquals(Actor.objects.get().name, actor['name'])

    def test_actor_name_is_unique(self):
        '''
        Test we cannot add an actor with the same exact name
        '''
        url = reverse('actor-list')
        actor = {'name': 'Mr Ultron'}
        response = self.client.post(url, actor, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        count_ = Actor.objects.count()
        response = self.client.post(url, actor, format='json')
        self.assertContains(response=response, text='actor with this name already exists.', count=1, status_code=status.HTTP_409_CONFLICT)
        self.assertEquals(count_, Actor.objects.count())

    def test_listing_actors(self):
        '''
        Test returning a list of actors
        '''
        url = reverse('actor-list')
        actors = Actor.objects.bulk_create([Actor(name='Mr Beast'), Actor(name='Josif Vissarionovič Stalin'), Actor(name='Robert Downey Jr.')])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.json()), len(actors))

    def test_listing_actors_is_empty(self):
        '''
        Test returning an empty list when there are no actors
        '''
        url = reverse('actor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.json()), 0)

    def test_retrieving_actor(self):
        '''
        Test retrieving an actor
        '''
        actor = {
            'name': 'Cuba Gooding Jr.'
        }
        actor = Actor.objects.create(**actor)
        url = reverse('actor-detail', args=[actor.id])
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['name'], actor.name)

    def test_retrieving_nonexisting_actor(self):
        '''
        Test retrieving an non exsiting actor
        '''
        url = reverse('actor-detail', args=[100])
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(response.json()['detail'], 'Actor does not exist')

    def test_updating_an_actor(self):
        '''
        Test updating an actor
        '''
        actor = Actor.objects.create(**{'name': 'Juan Carlos Bolanos'})
        self.assertEquals(actor.name, 'Juan Carlos Bolanos')
        url = reverse('actor-detail', args=[actor.id])
        actor.name = 'Sebastian Salas'
        serializer = ActorSerializer(actor, context={'request': None})
        response = self.client.put(url, serializer.to_representation(actor), format='json') # transform instance to dict
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['name'], actor.name)
        self.assertEquals(Actor.objects.count(), 1)

    def test_updating_actor_unique_name(self):
        '''
        Test updating an actor with non unique name
        '''
        actor = Actor.objects.create(**{'name': 'Juan Carlos Bolanos'})
        actor2 = Actor.objects.create(**{'name': 'Mama Lucha'})
        url = reverse('actor-detail', args=[actor.id])
        actor.name = 'Mama Lucha'
        serializer = ActorSerializer(actor, context={'request': None})
        response = self.client.put(url, serializer.to_representation(actor), format='json') # transform instance to dict
        self.assertContains(response=response, text='actor with this name already exists.', count=1, status_code=status.HTTP_409_CONFLICT)
        self.assertEquals(Actor.objects.count(), 2)
        self.assertEquals(Actor.objects.get(pk=actor.id).name, 'Juan Carlos Bolanos')
        self.assertEquals(Actor.objects.get(pk=actor2.id).name, actor2.name)

    def test_delete_actor(self):
        '''
        Test deleting an actor
        '''
        actors = Actor.objects.bulk_create([Actor(name='Mauricio Sanchez'), Actor(name='Juana la cubana')])
        url = reverse('actor-detail', args=[actors[0].id])
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Actor.objects.count(), 1)
        self.assertRaises(Actor.DoesNotExist, Actor.objects.get, pk=actors[0].id)
        # with self.assertRaises(Actor.DoesNotExist): # same as previous line
        #     Actor.objects.get(pk=actors[0].id)
    
    def test_delete_nonexisting_actor(self):
        '''
        Test deleting nonexisting actor
        '''
        url = reverse('actor-detail', args=[3])
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(Actor.objects.count(), 0)
