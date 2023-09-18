from __future__ import annotations

from django.db import models

from django_ltree.models import TreeModel


class Taxonomy(TreeModel):
    label_size = 2

    name = models.TextField()

    label_field = "name"

    def __str__(self):
        return f"{self.path}: {self.name}"


class NoLabel(TreeModel):
    # No 'label_field' defined here on purpose
    name = models.TextField()
