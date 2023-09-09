from django.core.exceptions import ImproperlyConfigured
from django.db import models

from .fields import PathField, PathValue
from .managers import TreeManager


class TreeModel(models.Model):
    path = PathField(unique=True)
    objects = TreeManager()

    class Meta:
        abstract = True
        ordering = ("path",)

    def get_label_field(self):
        if label_field := getattr(self, 'label_field', None):
            return label_field
        else:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} has not defined a 'label_field'"
            )

    def label(self):
        return self.path[-1]

    def get_ancestors_paths(self):  # type: () -> List[List[str]]
        return [
            PathValue(self.path[:n])
            for n, p in enumerate(self.path)
            if n > 0
        ]

    def ancestors(self):
        return type(self)._default_manager.filter(path__ancestors=self.path)

    def descendants(self):
        return type(self)._default_manager.filter(path__descendants=self.path)

    def parent(self):
        if len(self.path) > 1:
            return self.ancestors().exclude(id=self.id).last()

    def children(self):
        return self.descendants().filter(path__depth=len(self.path) + 1)

    def siblings(self):
        parent = self.path[:-1]
        return (
            type(self)
            ._default_manager.filter(path__descendants=".".join(parent))
            .filter(path__depth=len(self.path))
            .exclude(path=self.path)
        )

    def add_child(self, **kwargs):  # type: (Any) -> Any
        label_field = self.get_label_field()

        if label_field not in kwargs:
            raise ImproperlyConfigured(
                f"'{label_field}' must be provided in kwargs to add a child."
            )

        label_value = kwargs[label_field]

        if 'path' in kwargs:
            raise ImproperlyConfigured(
                "'path' should not be provided in kwargs, it will be automatically set."
            )

        kwargs['path'] = self.path[:]  # Assuming self.path is a list
        kwargs['path'].append(label_value)

        return type(self)._default_manager.create(**kwargs)
