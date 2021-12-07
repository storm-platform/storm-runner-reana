# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job-reana is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Plugin for the Storm Job to enable experiments execution on REANA instances."""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = []

extras_require = {
    "docs": [
        "Sphinx>=3,<4",
    ],
    "tests": tests_require,
    # Reprozip
    "reprozip-cli": [
        # Reprozip dependencies
        "rpaths>=1.0.0,<1.1",
        "reprounzip>=1.1,<2.0",
    ],
    "reprozip-service": [
        # General
        "pydash>=5.1.0,<6.0",
        "docker-py>=1.10.6,<2.0",
        # Reana
        "reana-client==0.8.0",
        "reana-commons @ git+https://github.com/storm-platform/tp-reana-commons",  # Modified for the storm platform.
        # Storm
        "storm-pipeline @ git+https://github.com/storm-platform/storm-pipeline",
    ],
    "service-base": [
        # Storm
        "storm-compendium @ git+https://github.com/storm-platform/storm-compendium",
    ],
}

extras_require["all"] = [req for _, reqs in extras_require.items() for req in reqs]

setup_requires = []

install_requires = [
    # General dependencies
    "click>=7.1.0",
]


packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("storm_job_reana", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="storm-job-reana",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords=[
        "Utility",
        "Reproducible Research",
        "ReproZip",
        "Reana",
        "Storm Platform",
    ],
    license="MIT",
    author="Felipe Menino Carlos",
    author_email="felipe.carlos@inpe.br",
    url="https://github.com/storm-platform/storm-job-reana",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "console_scripts": ["storm-job-reana = storm_job_reana.cli:cli"],
        "storm_job.plugins": [
            "storm-job-reana-reprozip = storm_job_reana.modules.reprozip:job_service_metadata"
        ],
        "invenio_db.models": [
            "storm_job_reana_docker_models = storm_job_reana.modules.environment.docker"
        ],
        "invenio_celery.tasks": [
            "storm_job_reana = storm_job_reana.modules.reprozip.service.workflow.serial",
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 1 - Planning",
    ],
)
