from setuptools import setup

setup(
    name="django-pypal",
    version="0.0.1",
    description="Django app for PyPal",
    keywords="django, pypal, paypal",
    author="Jared Morse",
    author_email="jarcoal@gmail.com",
    url="https://github.com/jarcoal/django-pypal",
    license="BSD",
    packages=["django_pypal"],
    zip_safe=False,
    install_requires=['django'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)