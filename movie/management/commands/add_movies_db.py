from django.core.management.base import BaseCommand
from movie.models import Movie
import json

class Command(BaseCommand):
    help = 'Load movies into the database'

    def handle(self, *args, **kwargs):
        json_file_path = 'movie/management/commands/movies.json'

        with open(json_file_path, 'r') as file:
            movie_data = json.load(file)

        for i in range(100):
            movie = movie_data[i]
            exist = Movie.objects.filter(title=movie['title']).first()
            if not exist:
                Movie.objects.create(
                    title=movie['title'],
                    image='movie/images/Captura.jpg',
                    genre=movie['genre'],
                    year=movie['year']
                )
