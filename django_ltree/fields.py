from typing import List, Union

from django import forms
from django.core.validators import RegexValidator
from django.db.models.fields import TextField
from django.forms.widgets import TextInput


class PathValue(List):
    def __init__(self, val: Union[list, str]):
        if isinstance(val, str):
            val = val.split(".")
        elif isinstance(val, list):
            val = val
        else:
            raise ValueError(f"Invalid value for path: {val!r}")

        super().__init__(val)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return ".".join(self)


class PathValueProxy:
    def __init__(self, field_name: str):
        self.field_name = field_name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        value = instance.__dict__[self.field_name]

        if value is None:
            return value

        return PathValue(instance.__dict__[self.field_name])

    def __set__(self, instance, value):
        if instance is None:
            return self

        instance.__dict__[self.field_name] = value


path_label_validator = RegexValidator(
    r"^[A-Za-z0-9_.]+$",
    "A label is a sequence of alphanumeric characters and underscores separated by dots.",
    "invalid",
)


class PathFormField(forms.CharField):
    default_validators = [path_label_validator]


class PathField(TextField):
    default_validators = [path_label_validator]

    def db_type(self, connection):
        return "ltree"

    def formfield(self, **kwargs):
        kwargs["form_class"] = PathFormField
        kwargs["widget"] = TextInput(attrs={"class": "vTextField"})
        return super().formfield(**kwargs)

    def contribute_to_class(self, cls, name, private_only=False):
        super().contribute_to_class(cls, name)
        setattr(cls, self.name, PathValueProxy(self.name))

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return PathValue(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        return str(PathValue(value))

    def to_python(self, value):
        if value is None:
            return value
        elif isinstance(value, PathValue):
            return value

        return PathValue(value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is None:
            return value
        elif isinstance(value, PathValue):
            return str(value)
        elif isinstance(value, (list, str)):
            return str(PathValue(value))

        raise ValueError(f"Unknwon value type {type(value)}")