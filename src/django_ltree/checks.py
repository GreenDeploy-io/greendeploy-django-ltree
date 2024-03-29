from __future__ import annotations

from django.core.checks import Warning as DjangoWarning
from django.core.checks import register


@register
def check_database_backend_is_postgres(app_configs, **kwargs):
    from django.conf import settings

    errors = []
    valid_dbs = ["postgres", "postgis"]

    if "default" in settings.DATABASES and all(
        d not in settings.DATABASES["default"]["ENGINE"] for d in valid_dbs
    ):
        errors.append(
            DjangoWarning(
                "django_ltree needs postgres to support install the ltree extension.",
                hint="Use the postgres engine or ignore if you already use a custom engine for postgres",
                id="django_ltree.W001",  # This is the ID
            )
        )

    return errors
