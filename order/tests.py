from django.test import TestCase
from .models import Order
from .serializers import OrderSerializer


class OrderTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        Order.objects.create(
            number=10,
            amount=10,
            wheigth=10,
            width=10,
            height=10,
            length=10,
            zip_from="12345678",
            zip_to="12345678",
        )
        Order.objects.create(
            number=20,
            amount=200,
            wheigth=200,
            width=200,
            height=20,
            length=20,
            zip_from="12345678",
            zip_to="12345678",
        )

    def test_something_that_will_pass(self):
        one = Order.objects.get(id=1)
        two = Order.objects.get(id=2)
        self.assertEqual(one.id, 1)
        self.assertEqual(two.id, 2)
        self.assertEqual(one.zip_from, two.zip_from)
        self.assertNotEqual(one.number, two.number)

    def test_model_roles(self):
        max_length_from = Order.objects.get(id=1)._meta.get_field("zip_from").max_length
        max_length_to = Order.objects.get(id=1)._meta.get_field("zip_from").max_length
        self.assertEqual(max_length_from, 8)
        self.assertEqual(max_length_to, 8)

    def test_something_that_will_fail(self):
        try:
            Order.objects.create(
                number=20,
                amount=500,
                wheigth=200,
                width=200,
                height=20,
                length="",
                zip_from="12345678",
                zip_to="12345678",
            )
        except Exception as error:
            error_response = str(error)
            self.assertEqual(
                error_response,
                """['“” value must be a decimal number.']""",
            )

    def test_zip_from_and_zip_to_cant_be_nullable(self):
        tree = {
            "number": 20,
            "amount": 500,
            "wheigth": 200,
            "width": 200,
            "height": 20,
            "length": 100,
            "zip_from": None,
            "zip_to": None,
        }
        serilizer = OrderSerializer(data=tree)
        self.assertFalse(serilizer.is_valid(raise_exception=False))

    def zip_field_must_have_a_minimum_length_of_8_characters(self):
        tree = {
            "number": 20,
            "amount": 500,
            "wheigth": 200,
            "width": 200,
            "height": 20,
            "length": 100,
            "zip_from": "None",
            "zip_to": "None",
        }
        serilizer = OrderSerializer(data=tree)
        self.assertFalse(serilizer.is_valid(raise_exception=False))
