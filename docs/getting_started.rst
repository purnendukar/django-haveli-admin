===============
Getting Started
===============

++++++++++++
Installation
++++++++++++

1. You can get stable version of Django Haveli Admin by using pip or easy_install::

    pip install django_haveli_admin

2. You will need to add the ``'django_haveli_admin'`` application to the ``INSTALLED_APPS`` setting of your Django project ``settings.py`` file::

    INSTALLED_APPS = [
        ...
        'django_haveli_admin',
        'django.contrib.admin',
    ]

.. important:: ``'django_haveli_admin'`` must be added before ``'django.contrib.admin'`` and if you are using third-party apps with special admin support.

++++++++++
Deployment
++++++++++

Deployment with Django Haveli Admin should not be different than any other Django application. If you have problems with deployment on production, read `Django docs on wsgi
<https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/>`_ first.

.. note:: If you deploy your project with Apache or ``Debug=False`` don’t forget to run ``./manage.py collectstatic``.

