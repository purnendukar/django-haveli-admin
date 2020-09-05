from django.conf import settings
from django import template

# Depending on your django version, `reverse` and `NoReverseMatch` has been moved.
# From django 2.0 they've been moved to `django.urls`
try:
    from django.urls import reverse, NoReverseMatch
except ImportError:
    from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()

# From django 1.9 `assignment_tag` is deprecated in favour of `simple_tag`
try:
    simple_tag = register.simple_tag
except AttributeError:
    simple_tag = register.assignment_tag

    