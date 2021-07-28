from django.core.management.base import BaseCommand, CommandError
from .common_mock import CommonMock

class Command(BaseCommand):

    def handle(self, *args, **options):
        CommonMock().execute()
        self.stdout.write(self.style.SUCCESS('Common data loaded successfully!'))