from django.contrib import admin
from .models import Order
from freight.serializers import CreateNewFreight
from datetime import datetime, timedelta
from typing import List


class OrderAdmin(admin.ModelAdmin):
    actions = ["make_call_api"]

    @admin.action(description="delivery coust")
    def make_call_api(self, request, queryset: List[Order]):
        now_date = datetime.now()

        for obj in queryset:
            response = obj.delivery_calculation()
            for carrier_data in response:
                if "error" in carrier_data.keys():
                    continue
                delivery_time = int(carrier_data["delivery_time"])
                delivery_date = now_date + timedelta(days=delivery_time)
                freight_data = {
                    "carrier": carrier_data["name"],
                    "delivery_time": delivery_date.strftime("%Y-%m-%d"),
                    "delivery_coust": carrier_data["price"],
                }

                serializer = CreateNewFreight(data=freight_data)
                serializer.is_valid(raise_exception=True)
                serializer.save(order=obj)


admin.site.register(Order, OrderAdmin)
