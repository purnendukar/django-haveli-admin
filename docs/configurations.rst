==============
Configurations
==============

+++++++++++++++++++++++++
App Icon in Sidebar
+++++++++++++++++++++++++

Add ``SHOW_NAV_APP_ICON`` in ``settings.py`` with boolean value ``True`` or ``False``
to enable to disable the app icon in sidebar menu. By default value of ``SHOW_NAV_APP_ICON``
is ``False`` to enable the icon set value to ``True``.::

    SHOW_NAV_APP_ICON = True  

+++++++++++++++++++++++++
Brand Image
+++++++++++++++++++++++++

If you wanted to add a brand image instead of header title in brand secttion.
Then add the value for ``SHOW_BRAND_IMAGE`` in ``settings.py`` as ``True`` or ``False`` to show
brand image in hader or not. Once you set the value ``SHOW_BRAND_IMAGE = True``
add the path in ``BRAND_IMAGE``.::

    SHOW_BRAND_IMAGE = True
    BRAND_IMAGE = "/images/branding.png"

.. note:: Image path given in ``BRAND_IMAGE`` is relative path to ``STATIC`` folder.


+++++++++
Examples:
+++++++++

In ``settings.py``::

    # Brand Image
    SHOW_BRAND_IMAGE = True
    BRAND_IMAGE = "/images/branding.png"

    # To show app icon in sidebar 
    SHOW_NAV_APP_ICON = True 


