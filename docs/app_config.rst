==============
App Config
==============

+++++++++++++++++++++++++
App Icon for Sidebar
+++++++++++++++++++++++++

To add the icon in sidebar for each app use ``icon`` attribute in ``AppConfig``
for each app in ``your_app/apps.py``. In ``icon`` attribute path of the image will 
be stored.::

    icon = 'images/auth_icon.png'

.. note:: Image path stored in ``icon`` should be relative path to ``STATIC`` file path value set in ``settings.py``.

**Example** (in ``your_app/apps.py``)::

    from django.apps import AppConfig

    class TestAppConfig(AppConfig):
        name = 'test_app'
        icon = 'images/auth_icon.png' # path realtive to static path set

.. note:: Make sure you have set the configuration ``SHOW_NAV_APP_ICON=True`` in ``settings.py`` to display icon in sidebar.



