# Generated by Django 4.2.11 on 2024-03-12 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("name", models.CharField(max_length=200, unique=True)),
                ("address", models.CharField(max_length=1000)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="MeasurementPoint",
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
                ("name", models.CharField(max_length=200, unique=True)),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="points",
                        to="measurements.location",
                    ),
                ),
            ],
            options={
                "unique_together": {("location", "name")},
            },
        ),
        migrations.CreateModel(
            name="WaterFlowMeasurement",
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
                ("timestamp", models.DateTimeField()),
                ("duration_ms", models.IntegerField()),
                ("volume_ml", models.PositiveBigIntegerField()),
                ("temperature_min_celsius", models.IntegerField()),
                ("temperature_avg_celsius", models.IntegerField()),
                ("temperature_max_celsius", models.IntegerField()),
                (
                    "measurement_point",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="water_flow_measurements",
                        to="measurements.measurementpoint",
                    ),
                ),
            ],
        ),
    ]