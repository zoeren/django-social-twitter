#!/usr/bin/env python

from setuptools import setup, find_packages


def readall(path):
    with open(path, encoding="utf-8") as fp:
        return fp.read()


setup(
    name="django-social-twitter",
    version="0.0.1",
    description="A server side twitter integration for django applications.",
    long_description=readall("README.rst"),
    author="Sören Spindler",
    author_email="soeren.s89@googlemail.com",
    url="https://github.com/zoeren/django-social-twitter",
    license="BSD License",
    packages=find_packages(exclude=("tests.*", "tests", "example")),
    install_requires=["django>=2.0", "python-twitter>=3.5"],
    python_requires=">=2.7",
    include_package_data=True,
    classifiers=[
        # "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Social Media :: Twitter',
    ],
)

# zip_safe=False,  # because we're including static files
# download_url=???

