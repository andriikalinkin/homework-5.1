from django.core.management.base import BaseCommand
from faker import Faker

from app.models import Teacher

fake = Faker()


class Command(BaseCommand):
    help = "Add the specify number of teachers to the database (default: 100)"

    def add_arguments(self, parser):
        parser.add_argument(
            "number",
            nargs="?",
            type=int,
            default=100,
            help="Number of teachers to create (default: 100)",
        )

    def handle(self, *args, **options):
        number_of_teachers = options["number"] or 100

        for i in range(number_of_teachers):
            t = Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                subject=fake.job(),
            )

            self.stdout.write(
                self.style.SUCCESS('Successfully added teacher "%s"' % t.id)
            )
