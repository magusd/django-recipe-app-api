"""
wait for db to be availble
"""
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Django command to wait for the db
    """

    def handle(self, *args, **options):
        self.stdout.write('Waiting for db...')
        db_up = False
        # max_tries = 30
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError) as e:
                self.stdout.write('Db unavailable, waiting 1s...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Connected to db'))

