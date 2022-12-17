from django.test import TestCase
from django.urls import reverse

from ProjectDefence.products.models import Product


class BaseTestCase(TestCase):
    def assertCollectionEqual(self, collection, message=None):
        return self.assertEqual(0, len(collection), message)


# Create your tests here.
class LaptopsListViewTests(BaseTestCase):
    def test_laptops_list_view__when_no_laptops__expect_empty_list(self):
        response = self.client.get(reverse('laptops'))
        self.assertCollectionEqual(response.context['laptops'])

    def test_laptops_list_view__when_laptops__expect_list_of_laptops(self):
        laptops_count = 3
        laptops = [Product(
            choice='Laptop',
            name=f'Test name{i}',
            make=f'Test make{i}',
            price=10.25 + i,
            image='https://ichef.bbci.co.uk/news/1024/branded_news/0347/production/_92593800_gettyimages-482923234.jpg',
            weight=1.50,
            description=f'asdasdasdasdasd'
        )
            for i in range(1, laptops_count + 1)
        ]
        Product.objects.bulk_create(laptops)
        response = self.client.get(reverse('laptops'))
        self.assertListEqual(laptops, list(response.context['laptops']))


class PhonesListViewTests(BaseTestCase):
    def test_phones_list_view__when_no_phones__expect_empty_list(self):
        response = self.client.get(reverse('phones'))
        self.assertCollectionEqual(response.context['phones'])

    def test_phones_list_view__when_phones__expect_list_of_laptops(self):
        phones_count = 3
        phones = [Product(
            choice='Phone',
            name=f'Test name{i}',
            make=f'Test make{i}',
            price=10.25 + i,
            image='https://ichef.bbci.co.uk/news/1024/branded_news/0347/production/_92593800_gettyimages-482923234.jpg',
            weight=1.50,
            description=f'asdasdasdasdasd'
        )
            for i in range(1, phones_count + 1)
        ]
        Product.objects.bulk_create(phones)
        response = self.client.get(reverse('phones'))
        self.assertListEqual(phones, list(response.context['phones']))


class ConsolesListViewTests(BaseTestCase):
    def test_consoles_list_view__when_no_consoles__expect_empty_list(self):
        response = self.client.get(reverse('consoles'))
        self.assertCollectionEqual(response.context['consoles'])

    def test_consoles_list_view__when_consoles__expect_list_of_laptops(self):
        consoles_count = 3
        consoles = [Product(
            choice='Console',
            name=f'Test name{i}',
            make=f'Test make{i}',
            price=10.25 + i,
            image='https://ichef.bbci.co.uk/news/1024/branded_news/0347/production/_92593800_gettyimages-482923234.jpg',
            weight=1.50,
            description=f'asdasdasdasdasd'
        )
            for i in range(1, consoles_count + 1)
        ]
        Product.objects.bulk_create(consoles)
        response = self.client.get(reverse('consoles'))
        self.assertListEqual(consoles, list(response.context['consoles']))


class AllProductsListViewTests(BaseTestCase):
    def test_all_products_list_view__when_no_products__expect_empty_list(self):
        response = self.client.get(reverse('latest products'))
        self.assertCollectionEqual(response.context['products'])

    def test_consoles_list_view__when_consoles__expect_list_of_laptops(self):
        products_count = 3
        products = [Product(
            choice='Console',
            name=f'Test name{i}',
            make=f'Test make{i}',
            price=10.25 + i,
            image='https://ichef.bbci.co.uk/news/1024/branded_news/0347/production/_92593800_gettyimages-482923234.jpg',
            weight=1.50,
            description=f'asdasdasdasdasd'
        )
            for i in range(1, products_count + 1)
        ]
        Product.objects.bulk_create(products)
        response = self.client.get(reverse('latest products'))
        self.assertListEqual(products, list(response.context['products']))
