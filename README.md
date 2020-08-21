# django-ltree

A tree extension implementation to support hierarchical tree-like data in Django models,
using the native Postgres extension `ltree`.

Postgresql has already a optimized and very useful tree implementation for data.
The extension is [ltree](https://www.postgresql.org/docs/9.6/static/ltree.html)

This fork contains a backport to Django 1.11 and Python 2.7.

[![Build Status](https://travis-ci.org/mariocesar/django-ltree.svg?branch=master)](https://travis-ci.org/mariocesar/django-ltree)

[![codecov](https://codecov.io/gh/mariocesar/django-ltree/branch/master/graph/badge.svg)](https://codecov.io/gh/mariocesar/django-ltree)

[![Coverage Status](https://coveralls.io/repos/github/mariocesar/django-ltree/badge.svg?branch=master)](https://coveralls.io/github/mariocesar/django-ltree?branch=master)


## Links

 - Pypi https://pypi.org/project/django-ltree/
 - Source code https://github.com/mariocesar/django-ltree
 - Bugs https://github.com/mariocesar/django-ltree/issues
 - Contribute https://github.com/mariocesar/django-ltree/pulls
 - Documentation `TODO`

## Install

```
pip install django-ltree
```

Then add `django_ltree` to `INSTALLED_APPS` in your Django project settings.

And make sure to run `django_ltree` migrations before you added the `PathField`

```
python manage.py migrate django_ltree
```

`django_ltree` migrations will install the `ltree` extension if not exist.

You can alternatively specify the `django_ltree` dependency in the migrations of
your applications that requires `PathField`, and run migrations smoothly.

```
class Migration(migrations.Migration):
    dependencies = [
            ('django_ltree', '__latest__'),
    ]
```

## Requires

- Django 1.11 or superior
- Python 2

## Testing

Make sure you have Postgres installed. Then simply run `tox` in the root directory of the project.
