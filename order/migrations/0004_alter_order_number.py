# Generated by Django 4.2.3 on 2023-07-28 01:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0003_alter_order_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="number",
            field=models.UUIDField(auto_created=True, default=uuid.uuid4),
        ),
    ]
