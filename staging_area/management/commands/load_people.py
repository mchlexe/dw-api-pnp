from csv import DictReader
from django.core.management import BaseCommand
from staging_area.models import Person


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Load data from people.csv"

    def handle(self, *args, **options):

        if Person.objects.exists():
            print('people data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        print("Loading people data")

        for row in DictReader(open('./csv/people.csv')):
            person = Person(name=row['Name'], sex=row['Sex'], age=row['Age'])
            person.save()
