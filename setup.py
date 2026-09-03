# -*- coding: utf-8 -*-

import setuptools

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tjzegmott-python-logging-loki",
    version="0.0.1",
    description="Python logging handler for Grafana Loki",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Roman Rapoport",
    author_email="cryos10@gmail.com",
    url="https://github.com/tjzegmott/python-logging-loki",
    packages=setuptools.find_packages(exclude=("tests",)),
    python_requires=">=3.8.1,<4.0",
    install_requires=["rfc3339>=6.1", "requests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
