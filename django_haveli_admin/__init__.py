__version__ = '0.0.3'

from django.contrib.auth import apps

setattr(apps.AuthConfig,'icon','images/auth_icon.png')
