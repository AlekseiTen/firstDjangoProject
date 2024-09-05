from django.core.management import BaseCommand
import json
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open('catalog.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):

        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['name'], description=category['description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product['name'], description=product['description'], created_at=product[' created_at'],
                        # получаем категорию из базы данных для корректной связки объектов
                        category=Category.objects.get(pk=product['category']))
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
