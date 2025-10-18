import csv
from django.core.management.base import BaseCommand
from shop.models import Product

class Command(BaseCommand):
    help = 'Import products from CSV (name, price, description)'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    price = float(row['price'])
                    Product.objects.create(
                        name=row['name'],
                        price=price,
                        description=row['description']
                    )
                except Exception as e:
                    self.stderr.write(f"Error importing row: {row} — {e}")

        self.stdout.write(self.style.SUCCESS('✅ Products successfully imported!'))
