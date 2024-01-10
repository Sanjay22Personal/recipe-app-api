"""
Django command to wait for the database to be available
"""

from django.core.managemment.base import BaseCommand

class Command(BaseCommand):
    """Command to wait from database."""

    def handle(self, *args, **options):
        pass