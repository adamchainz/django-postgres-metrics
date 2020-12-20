import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="django-postgres-metrics",
    author="Markus Holtermann",
    author_email="info@markusholtermann.eu",
    description="A Django app that exposes a bunch of PostgreSQL database metrics.",
    license="BSD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/django-postgres-metrics/django-postgres-metrics",
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    include_package_data=True,
    extras_require={
        "dev": ["pre-commit"],
        "docs": [
            "Django",
            "psycopg2",
            "sphinx_rtd_theme",
            "Sphinx>=3.0,<3.4",
        ],
        "test": [
            "coverage[toml]>=5,<6",
            "Django",
            "psycopg2",
        ],
    },
    setup_requires=["setuptools_scm>=5<6"],
    use_scm_version=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.5",
)
