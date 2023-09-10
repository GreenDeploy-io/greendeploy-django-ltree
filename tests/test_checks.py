import os

import pytest

from django_ltree.checks import check_database_backend_is_postgres


# Test when the database engine is Postgres
@pytest.mark.filterwarnings("ignore:Overriding setting DATABASES can lead to unexpected behavior.")
def test_database_is_postgres(settings):
    settings.DATABASES = {
        'default': {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DJANGO_DATABASE_NAME", "ltree_test"),
            "HOST": os.environ.get("DJANGO_DATABASE_HOST", "localhost"),
            "USER": os.environ.get("DJANGO_DATABASE_USER", "postgres"),
            "PASSWORD": os.environ.get("DJANGO_DATABASE_PASSWORD", "postgres")
        }
    }
    errors = check_database_backend_is_postgres(None)
    assert len(errors) == 0

# Test when the database engine is not Postgres
@pytest.mark.filterwarnings("ignore:Overriding setting DATABASES can lead to unexpected behavior.")
def test_database_is_not_postgres(settings):
    settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
            # ... other settings ...
        }
    }
    errors = check_database_backend_is_postgres(None)
    assert len(errors) == 1
    assert errors[0].id == 'django_ltree.W001'  # Replace 'your_app.W001' with the actual id of the Warning.
