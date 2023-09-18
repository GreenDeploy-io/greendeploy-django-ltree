# Generated by Django 1.11.24 on 2019-09-11 12:31
from __future__ import annotations

from django.db import migrations
from django.db import models

import django_ltree.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Taxonomy",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("path", django_ltree.fields.PathField(unique=True)),
                ("name", models.TextField()),
            ],
            options={
                "ordering": ("path",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="NoLabel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("path", django_ltree.fields.PathField(unique=True)),
                ("name", models.TextField()),
            ],
            options={
                "ordering": ("path",),
                "abstract": False,
            },
        ),
    ]
