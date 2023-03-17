# Generated by Django 4.1.7 on 2023-03-17 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("classified", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Opinion",
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
                ("rating", models.IntegerField()),
                ("op", models.CharField(max_length=1000)),
                (
                    "employer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="classified.employer",
                    ),
                ),
                (
                    "worker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="classified.worker",
                    ),
                ),
            ],
        ),
    ]