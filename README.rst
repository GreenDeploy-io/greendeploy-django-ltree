===================
greendeploy-django-ltree
===================

.. image:: https://img.shields.io/github/actions/workflow/status/GreenDeploy-io/greendeploy-django-ltree/main.yml?branch=main&style=for-the-badge
   :target: https://github.com/GreenDeploy-io/greendeploy-django-ltree/actions?workflow=CI

.. image:: https://img.shields.io/badge/Coverage-100%25-success?style=for-the-badge
  :target: https://github.com/GreenDeploy-io/greendeploy-django-ltree/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/greendeploy-django-ltree.svg?style=for-the-badge
    :target: https://pypi.org/project/greendeploy-django-ltree/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
    :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

The authoritative and broadly useful Django package for using Postgres
ltree fields in your Django models, designed to be transparent and
accessible for Django beginners.

Welcome
-------

Welcome to greendeploy-django-ltree, your go-to package for handling PostgreSQL
ltree fields in a Django project. We're mindful of the end-to-end context and
aim to make this package not just a code repository but **a complete learning
experience**.

We aim to achieve this in three ways:

1. **Beginner-friendly documentation**: We specifically tailor the
    documentation to help Django newcomers and include end-to-end
    demonstrations that make no assumptions about your prior knowledge of
    ltree or materialized paths.

2. **Quick, early wins in 10 mins each**: We have picked 3 base cases as early
    wins for you. Each of these should take you no more than 10 mins to
    complete, including reading the docs.

    - **Install in sandbox project**: We show you how to install the package
        in a sandbox project and create the field in your Postgres database.
    - **Add materialized path in ltree field**: We show you how to add data
        to your ltree field using your Django ORM.
    - **Query ltree field**: We show you how to query your ltree field using
        Django ORM.

3. **Active maintenance**: We are committed to maintaining this package and
    keeping it up to date with the latest Django, Python, and Postgres versions.
    We have plans to measure the mean time to close the Github issues and will
    reveal them in the near future.

About ltree
------------

`ltree` is a data type in Postgres database. It is a tree-like structure
where each node is a __label__. The label can be a string or a number.

Thus, the piece of data is basically a **string of labels separated by dots**.
Also known as a __label__ __path__.

A label consists of `A-Za-z0-9_` and can be up to 255 characters long.

The length of a label path is a maximum 65535 labels long.

An example of a label path is `Top.Countries.Europe.Russia` where `Top` is the
root node and `Russia` is the leaf node.

There's another name for label path that's more better known which is
`Materialized Path` coined by `Vadim Tropashko <http://vadimtropashko.wordpress.com/>`__
in `SQL Design Patterns <http://www.rampant-books.com/book_0601_sql_coding_styles.htm>`__.

Some good resources to read on the subject are:

* Postgres' own `documentation <https://www.postgresql.org/docs/current/ltree.html>`__
* Vadim Tropashko's `Nested Sets and Materialized Path SQL Trees <http://www.rampant-books.com/art_vadim_nested_sets_sql_trees.htm>`__
* `django-treebeard`'s `Materialized Path trees <https://django-treebeard.readthedocs.io/en/latest/mp_tree.html>`_


Requirements
------------

Postgres 15 supported.

Python 3.8 to 3.11 supported.

Django 4.2 supported.


----

Setup
-----

Install from **pip**:

.. code-block:: sh

    python -m pip install greendeploy-django-ltree

and then add it to your installed apps:

.. code-block:: python

    INSTALLED_APPS = [
        ...,
        "greendeploy-django-ltree",
        ...,
    ]

Make sure you add the trailing comma or you might get a ``ModuleNotFoundError``
(see `this blog
post <https://adamj.eu/tech/2020/06/29/why-does-python-raise-modulenotfounderror-when-modifying-installed-apps/>`__).

You will also need to run `django_ltree` migrations before you added the `PathField`.

See Quick Start below and in documentation for more details.


About
-----

**django-ltree** (`Github repository <https://github.com/mariocesar/django-ltree>`__) was
created in March 2020 by Mario-César. It went unmaintained from August 2021.

Kimsia Sim was motivated to fork it under the name **greendeploy-django-ltree** in September 2023
and make it support Django 4.2. The reason is that Kimsia needed to use it in a Django 4.2 project.

The pypi package name is under
`greendeploy-django-ltree <https://pypi.org/project/greendeploy-django-ltree/>`__ and formally
published on 11th September 2023.

**greendeploy-django-ltree** has had `close to 10 contributors
<https://github.com/greendeploy-io/greendeploy-django-ltree/graphs/contributors>`__
in its time; gratitude and a big thank you to every one of them.

Quick Start
-------------

@TODO: Add quick start here.