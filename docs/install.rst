============
Installation
============


Requirements
============

Before installing blanc-basic-assets, you'll need a copy of Django__ 1.8 or
later installed. Image uploads require the `Pillow`__ library installed.

.. __: http://www.djangoproject.com/
.. __: http://python-imaging.github.io/


Installing blanc-basic-assets
=============================

The fastest way of installing is to use pip__.

.. __: http://www.pip-installer.org/

Simply type::

    pip install blanc-basic-assets

Manual installation
-------------------

Alternative you manually install by downloading the latest version from the
`blanc-basic-assets page on the Python Package Index`__.

.. __: http://pypi.python.org/pypi/blanc-basic-assets/

Download the package, unpack it and run the ``setup.py`` installation
script::

    python setup.py install


Configuring your project
========================

Edit your Django project's settings module, and add ``blanc_basic_assets``::

    INSTALLED_APPS = (
        ...
        'blanc_basic_assets',
    )

Once this is done, run ``python manage.py migrate`` to update your database.
