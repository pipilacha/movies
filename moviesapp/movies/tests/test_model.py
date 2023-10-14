from django.test import TestCase

from movies.models import Movie

class Movies(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        data = {
            'title': 'Avengers 3',
            'gender': 'Comics',
            'rating': '4.5',
            'description': 'Avengers save the world',
            'release_date': '',
            'actors': 'list of actors',
            'image': 'url',
            'availability': 'Unreleased, Available, Not Avaible'

        }
        Movie.objects.create(**data)

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
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)


