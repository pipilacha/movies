from django.test import TestCase

from django.utils import timezone

from movies.models import Movies
from actors.models import Actor


class Test_Actors(TestCase):
    movies_id = []    

    @classmethod
    def setUpTestData(cls) -> None:
        print("Setting up test data for Actors model Tests")        
        actors = Actor.objects.bulk_create([Actor(name='Idris Elba'), Actor(name='Juan Mora'), Actor(name='Santa Claus')])
        data = {
            'title': 'Avengers 3',
            'rating': '4.5',
            'description': 'Avengers save the world',
            'release_date': timezone.now(),
            'image': 'https://static.wikia.nocookie.net/horadeaventura/images/1/1b/BMOGAME.png/revision/latest/thumbnail/width/360/height/360?cb=20150710131037&path-prefix=es',
            'availability': 'Unreleased, Available, Not Avaible'
        }
        movie = Movies.objects.create(**data)
        movie.actors.add(*actors)
        cls.movies_id.append(movie.id)

        idris_elba = list(filter(lambda x: x.name == 'Idris Elba', actors))[0] # this way we dont query the db again
        data['title'] = 'Married with kids'
        movie = Movies.objects.create(**data)
        movie.actors.add(idris_elba)
        cls.movies_id.append(movie.id)

    def test_many_to_many_rel_movies(self):
        actors = Actor.objects.get(name='Idris Elba')
        movies = Movies.objects.filter(actors=actors.id)
        self.assertEquals(len(movies), len(Test_Actors.movies_id))
        for movie in movies:
            self.assertIn(movie.id, Test_Actors.movies_id)
    
