# Generated by Django 4.2.3 on 2023-07-27 23:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_alter_order_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="number",
            field=models.UUIDField(auto_created=True, default=0),
        ),
    ]
