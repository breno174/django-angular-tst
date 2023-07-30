from django.test import TestCase
from .models import Freight
from order.models import Order
from datetime import date
import uuid


class FreightTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        order = Order.objects.create(
            number=10,
            amount=10,
            wheigth=10,
            width=10,
            height=10,
            length=10,
            zip_from="12345678",
            zip_to="12345678",
        )
        Freight.objects.create(
            carrier="carrier",
            delivery_time=date.fromisoformat("2019-12-04"),
            delivery_coust=55.5,
            external_freight_id=uuid.uuid4(),
            order=order,
        )

    def test_something_that_will_pass(self):
        ...

    def test_something_that_will_fail(self):
        ...
