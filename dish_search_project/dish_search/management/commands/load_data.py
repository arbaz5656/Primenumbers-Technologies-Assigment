# dish_search/management/commands/load_data.py

import csv
from django.core.management.base import BaseCommand
from dish_search.models import Restaurant

class Command(BaseCommand):
    help = 'Load data from CSV into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    restaurant = Restaurant(
                        id=row['id'],
                        name=row['name'],
                        location=row['location'],
                        items=row['items'],
                        lat_long=row['lat_long'],
                        full_details=row['full_details']
                    )
                    restaurant.save()
            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found at path: {file_path}"))
