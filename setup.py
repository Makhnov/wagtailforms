#!/usr/bin/env python

from codecs import open
from os import path

from setuptools import setup

from wagtailstreamforms import __version__

install_requires = [
    "wagtail>=5",
    "Unidecode>=1",
]

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="wagtailstreamforms",
    version=__version__,
    description="Wagtail forms in a streamfield",
    long_description=long_description,
    author="Stuart George",
    author_email="stuart@accentdesign.co.uk",
    url="https://github.com/AccentDesign/wagtailstreamforms/",
    download_url="https://pypi.python.org/pypi/wagtailstreamforms",
    license="MIT",
    packages=["wagtailstreamforms"],
    install_requires=install_requires,
    include_package_data=True,
    keywords=["wagtail", "streamfield", "forms", "accent", "design"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.12",
        "Framework :: Django :: 4.2",
        "Framework :: Wagtail :: 5",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ],
)
