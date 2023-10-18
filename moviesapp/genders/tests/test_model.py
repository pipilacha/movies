from django.test import TestCase

from django.utils import timezone

from movies.models import Movies
from genders.models import Genders

# Create your tests here.
class Test_Genders(TestCase):
    movies_id = []

    @classmethod
    def setUpTestData(cls) -> None:
        print("Setting up test data for Gender model Tests")        
        genders = Genders.objects.bulk_create([Genders(name='Horror'), Genders(name='Sci-Fi')])
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
        Test_Genders.movies_id.append(movie.id)

        sci_fi = Genders.objects.filter(name='Sci-Fi')
        data['title'] = 'Star Wars'
        movie = Movies.objects.create(**data)
        movie.genders.add(*sci_fi)
        Test_Genders.movies_id.append(movie.id)

    def test_many_to_many_rel_movies(self):
        gender = Genders.objects.get(name='Sci-Fi')
        movies = Movies.objects.filter(genders=gender.id)
        self.assertEquals(len(movies), len(Test_Genders.movies_id))
        for movie in movies:
            self.assertIn(movie.id, Test_Genders.movies_id)
    