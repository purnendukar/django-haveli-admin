__version__ = '0.1.0'

from django.contrib.auth import apps

setattr(apps.AuthConfig,'icon','images/auth_icon.png')
