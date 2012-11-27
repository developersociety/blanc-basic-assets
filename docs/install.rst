============
Installation
============

Requirements
============

Before installing blanc-basic-assets, you'll need a copy of Django__ 1.3 or
later installed. Image uploads require the `Python Imaging Library`__
installed.

.. __: http://www.djangoproject.com/
.. __: http://www.pythonware.com/products/pil/

The Django sites framework is also required to be installed.


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

Edit your Django project's settings module, ensure that
``django.contrib.sites`` is already added to ``INSTALLED_APPS``, and add
``blanc_basic_assets.assets``::

    INSTALLED_APPS = (
        'django.contrib.sites',
        ...
        'blanc_basic_assets.assets',
    )

Once this is done, run ``python manage.py syncdb`` to update your database.
