from .django_template_tags import *

from django.template.loader import get_template
from django.template import Context

try:
    # Python 3.
    from urllib.parse import parse_qs
except ImportError:
    # Python 2.5+
    from urlparse import urlparse

    try:
        # Python 2.6+
        from urlparse import parse_qs
    except ImportError:
        # Python <=2.5
        from cgi import parse_qs

@simple_tag
def haveli_list_filter_select(cl, spec):
    tpl = get_template(spec.template)
    choices = list(spec.choices(cl))
    field_key = spec.field_path if hasattr(spec, 'field_path') else \
        spec.parameter_name
    matched_key = field_key
    for choice in choices:
        query_string = choice['query_string'][1:]
        query_parts = parse_qs(query_string)

        value = ''
        matches = {}

        for key in query_parts.keys():
            if key == field_key:
                value = query_parts[key][0]
                matched_key = key
            elif key.startswith(field_key + '__') or '__' + field_key + '__' in key:
                value = query_parts[key][0]
                matched_key = key
            
            print('key',key)

            if value:
                matches[matched_key] = value

        # Iterate matches, use first as actual values, additional for hidden
        # i = 0
        for key, value in matches.items():
            choice['name'] = key
            choice['val'] = value
            choice['additional'] = '%s=%s' % (key, value)

    return tpl.render({
        'field_name': field_key,
        'title': spec.title,
        'choices': choices,
        'spec': spec,
    })