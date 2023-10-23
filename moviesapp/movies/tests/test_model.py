from django.test import TestCase

from django.utils import timezone

from movies.models import Movies
from actors.models import Actor
from genders.models import Genders


class Test_Movies(TestCase):
    movied_id = None
    @classmethod
    def setUpTestData(cls) -> None:
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        genders = Genders.objects.bulk_create([Genders(name='Horror'), Genders(name='Sci-Fi')])
        actors = Actor.objects.bulk_create([Actor(name='Chris Pratt'), Actor(name='Brad Pitt'), Actor(name='Santa Claus')])
        data = {
            'title': 'Avengers 3',
            'rating': '4.5',
            'description': 'Avengers save the world',
            'release_date': timezone.now(),
            'image': 'https://static.wikia.nocookie.net/horadeaventura/images/1/1b/BMOGAME.png/revision/latest/thumbnail/width/360/height/360?cb=20150710131037&path-prefix=es',
            'availability': 'Unreleased, Available, Not Avaible'
        }
        movie = Movies.objects.create(**data)
        movie.genders.add(*genders)
        movie.actors.add(*actors)
        Test_Movies.movied_id = movie.id

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass: Runs after all class methods are executed.")
        pass
    
    def setUp(self) -> None:
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def tearDown(self) -> None:
        print("tearDown: Runs after every test method")
        pass

    def test_title_max_length(self):
        movie = Movies.objects.get(id=Test_Movies.movied_id)
        max_length = movie._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_many_to_many_rel_genders(self):
        genders = Movies.objects.get(id=Test_Movies.movied_id).genders.all()
        for gender in genders:
            self.assertIn(gender.name, ['Horror', 'Sci-Fi'])

    def test_many_to_many_rel_actors(self):
        actors = Movies.objects.get(id=Test_Movies.movied_id).actors.all()
        for actor in actors:
            self.assertIn(actor.name, ['Chris Pratt', 'Brad Pitt', 'Santa Claus'])
