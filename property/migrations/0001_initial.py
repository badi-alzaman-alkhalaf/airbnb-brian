# Generated by Django 4.1 on 2023-07-26 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "icon",
                    models.ImageField(blank=True, null=True, upload_to="category/"),
                ),
                ("name", models.CharField(default="", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Property",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField(max_length=500)),
                ("image", models.ImageField(upload_to="property_images/")),
                ("price", models.IntegerField()),
                ("slug", models.SlugField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_category",
                        to="property.category",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PropertyPlace",
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
                ("name", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="place/")),
            ],
        ),
        migrations.CreateModel(
            name="PropertyReservation",
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
                ("date_from", models.DateField()),
                ("date_to", models.DateField()),
                (
                    "guest",
                    models.IntegerField(
                        choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        default=1,
                    ),
                ),
                (
                    "children",
                    models.IntegerField(
                        choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        default=1,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservation_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_reservation",
                        to="property.property",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PropertyRate",
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
                    "rate",
                    models.IntegerField(
                        choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        default=0,
                    ),
                ),
                ("feedback", models.TextField(default="", max_length=200)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rate_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_rates",
                        to="property.property",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PropertyImages",
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
                ("image", models.ImageField(upload_to="property_images/")),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_images",
                        to="property.property",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="property",
            name="place",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="property_place",
                to="property.propertyplace",
            ),
        ),
    ]
