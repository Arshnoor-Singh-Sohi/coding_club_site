# Generated by Django 5.2.1 on 2025-06-11 21:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_member"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="publisher",
            name="country",
            field=models.CharField(default="USA", max_length=20),
        ),
        migrations.AlterField(
            model_name="member",
            name="address",
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name="member",
            name="city",
            field=models.CharField(default="Windsor", max_length=20),
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order_type",
                    models.IntegerField(
                        choices=[(0, "Purchase"), (1, "Borrow")], default=1
                    ),
                ),
                ("order_date", models.DateField(default=django.utils.timezone.now)),
                ("books", models.ManyToManyField(to="myapp.book")),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.member"
                    ),
                ),
            ],
        ),
    ]
