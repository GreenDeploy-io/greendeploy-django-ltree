# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages


with open("README.rst", "r") as fh:
    long_description = fh.read()


setup(
    name="greendeploy-django-ltree",
    version="0.5.3",
    python_requires=">=2.7",
    url="https://github.com/GreenDeploy-io/greendeploy-django-ltree",
    author="KimSia Sim",
    author_email="kimsia@oppoin.com",
    description="Django app to support ltree postgres extension",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude=("example",)),
    extras_require={"develop": ["twine", "tox"]},
    install_requires=["django>=1.11", "six"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    project_urls={
        "Source": "https://github.com/GreenDeploy-io/greendeploy-django-ltree",
        "Tracker": "https://github.com/GreenDeploy-io/greendeploy-django-ltree/issues",
    },
)
