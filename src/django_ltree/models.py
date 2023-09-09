from django.core.exceptions import ImproperlyConfigured
from django.db import models

from .fields import PathField, PathValue
from .managers import TreeManager
from .paths import PathGenerator


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


    def add_child(self, **kwargs):
        label_field = self.get_label_field()

        if label_field not in kwargs:
            raise ImproperlyConfigured(
                f"'{label_field}' must be provided in kwargs to add a child."
            )

        # label_field value cannot be None
        if kwargs[label_field] is None:
            raise ImproperlyConfigured(
                f"'{label_field}' cannot be None."
            )

        if 'path' in kwargs:
            raise ImproperlyConfigured(
                "'path' should not be provided in kwargs, it will be automatically set."
            )

        # Generate the new path using the same logic as in TreeManager.create_child
        paths_in_use = self.children().values_list("path", flat=True)
        path_generator = PathGenerator(
            prefix=self.path,
            skip=paths_in_use,
            label_size=getattr(type(self), "label_size"),
        )
        kwargs["path"] = next(path_generator)  # updated to Python 3's next function

        return type(self)._default_manager.create(**kwargs)


