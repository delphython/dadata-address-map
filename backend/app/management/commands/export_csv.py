import csv

from django.core.management.base import BaseCommand

from app.models import Addresses

def export_addresses_from_csv(csv_file):
    pass


class Command(BaseCommand):
    help = 'Export addresses from csv file'


    def add_arguments(self, parser):
        parser.add_argument('cvs_file_path', type=str)


    def handle(self, *args, **options):
        csv_file_path = options['cvs_file_path']

        with open(csv_file_path, 'r', encoding = "UTF8", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header = next(reader)
            
            for row in reader:
                _object_dict = {key: value for key, value in zip(header, row)}
                Addresses.objects.get_or_create(**_object_dict)
