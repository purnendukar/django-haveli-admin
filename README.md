# Django Haveli Admin

![PyPI](https://img.shields.io/pypi/v/django-haveli-admin)
![GitHub](https://img.shields.io/github/license/purnendukar/django-haveli-admin)
[![Downloads](https://pepy.tech/badge/django-haveli-admin)](https://pepy.tech/project/django-haveli-admin)
[![Documentation Status](https://readthedocs.org/projects/django-haveli-admin/badge/?version=latest)](https://django-haveli-admin.readthedocs.io/en/latest/?badge=latest)
      

**Improved theme for Django admin Interface**.

Django Haveli Admin is alternative Theme for [Django](http://www.djangoproject.com) administration interface.

# License

* Django Haveli Admin is licensed under BSD-3-Clause license.


# Docs & Package

* Documentation: https://django-haveli-admin.readthedocs.io/en/latest/

* Package: https://pypi.org/project/django-haveli-admin/

# Requirement

* Django: 2.1 or above

# Usage

**project/settings.py**

Always place the above django's default admin package (django.contrib.admin). So that it could override the existin django theme.

```
INSTALLED_APPS = [

    'django_haveli_admin',
    'django.contrib.admin',
    ...
]
```

# What's New 

* sidebar menu whole tab clickable
* Can add icon in AppConfig for sidebar
* Can add Brand Image 
* User menu dropdown
* Added Home button in sidebar



# Sample

**Django Haveli Admin: Login**
![alt text](https://github.com/purnendukar/django-haveli-admin/blob/master/django_haveli_admin-sample/django_haveli_login.png?raw=true)

**Django Haveli Admin: Dashboard**
![alt text](https://github.com/purnendukar/django-haveli-admin/blob/master/django_haveli_admin-sample/django_haveli_branding.png?raw=true)

**Django Haveli Admin: Nav Sidebar and Dropdown**
![alt text](https://github.com/purnendukar/django-haveli-admin/blob/master/django_haveli_admin-sample/django_haveli_navicon_dropdown.png?raw=true)

**Django Haveli Admin: Filters**
![alt text](https://github.com/purnendukar/django-haveli-admin/blob/master/django_haveli_admin-sample/django_haveli_filters.png?raw=true)

**Django Haveli Admin: Change Form**
![alt text](https://github.com/purnendukar/django-haveli-admin/blob/master/django_haveli_admin-sample/django_haveli_changeform.png?raw=true)



