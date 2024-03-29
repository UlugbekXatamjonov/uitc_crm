# Generated by Django 4.2.1 on 2023-07-03 03:57

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("userapp", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Branch",
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
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="Nomi"),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False, populate_from="name", unique=True
                    ),
                ),
                ("adress", models.CharField(max_length=250, verbose_name="Manzil")),
                ("status", models.BooleanField(default=True, verbose_name="Holati")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Filial",
                "verbose_name_plural": "Filiallar",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Room",
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
                    "number",
                    models.PositiveIntegerField(default=1, verbose_name="Raqami"),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        populate_from=mainapp.models.slugify_two_fields,
                        unique=True,
                        verbose_name="slug",
                    ),
                ),
                (
                    "capacity",
                    models.PositiveIntegerField(default=8, verbose_name="Sig'imi"),
                ),
                ("status", models.BooleanField(default=True, verbose_name="Holati")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rooms",
                        to="mainapp.branch",
                        verbose_name="Filial",
                    ),
                ),
            ],
            options={
                "verbose_name": "Xona",
                "verbose_name_plural": "Xonalar",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Group",
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
                ("name", models.CharField(max_length=50, verbose_name="Nomi")),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False, populate_from="name", unique=True
                    ),
                ),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("toq", "Du-Chor-Ju"),
                            ("juft", "Se-Pay-Shan"),
                            ("boot", "Bootcamp"),
                        ],
                        default="toq",
                        max_length=25,
                    ),
                ),
                (
                    "time",
                    models.CharField(
                        choices=[
                            ("8", "8:00-11:00"),
                            ("12", "12:00-14:00"),
                            ("14", "14:00-17:00"),
                        ],
                        default="8",
                        max_length=25,
                    ),
                ),
                ("status", models.BooleanField(default=True, verbose_name="Holati")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="groups",
                        to="mainapp.branch",
                        verbose_name="Filial",
                    ),
                ),
                (
                    "field",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="groups",
                        to="userapp.field",
                        verbose_name="Kurs",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="groups",
                        to="mainapp.room",
                        verbose_name="xona",
                    ),
                ),
                (
                    "students",
                    models.ManyToManyField(
                        related_name="students",
                        to="userapp.student",
                        verbose_name="O'quvchilar",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="group",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="O'qtuvchi",
                    ),
                ),
            ],
            options={
                "verbose_name": "Guruh",
                "verbose_name_plural": "Guruhar",
                "ordering": ("-created_at",),
            },
        ),
    ]
