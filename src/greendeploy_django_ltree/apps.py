import importlib

from django.apps import AppConfig


def register_pathfield():
    # Register field checks, lookups and functions
    importlib.import_module("greendeploy_django_ltree.checks")
    importlib.import_module("greendeploy_django_ltree.lookups")
    importlib.import_module("greendeploy_django_ltree.functions")


class GreendeployDjangoLtreeConfig(AppConfig):
    name = "greendeploy_django_ltree"

    def ready(self):
        register_pathfield()
