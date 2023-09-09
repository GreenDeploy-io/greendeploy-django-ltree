from django.db import models

from django_ltree.models import TreeModel


class Taxonomy(TreeModel):
    label_size = 2

    name = models.TextField()

    label_field = 'name'

    def __str__(self):
        return f'{self.path}: {self.name}'
