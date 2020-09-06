from django.contrib.admin.sites  import AdminSite
from django.utils.text import capfirst
from django.apps import apps

from .utils import *

class HaveliAdminSite(AdminSite):

    enable_nav_sidebar = True

    def each_context(self, request):
        """
        Return a dictionary of variables to put in the template context for
        *every* page in the admin site.
        For sites running on a subpath, use the SCRIPT_NAME value if site_url
        hasn't been customized.
        """
        script_name = request.META['SCRIPT_NAME']
        site_url = script_name if self.site_url == '/' and script_name else self.site_url
        return {
            'site_title': self.site_title,
            'site_header': self.site_header,
            'site_url': site_url,
            'has_permission': self.has_permission(request),
            'available_apps': self.get_app_list(request),
            'is_popup': False,
            'is_nav_sidebar_enabled': self.enable_nav_sidebar,
        }
    
    def _build_app_dict(self, request, label=None):
        """
        Build the app dictionary. The optional `label` parameter filters models
        of a specific app.
        """
        app_dict = {}

        if label:
            models = {
                m: m_a for m, m_a in self._registry.items()
                if m._meta.app_label == label
            }
        else:
            models = self._registry

        for model, model_admin in models.items():
            app_label = model._meta.app_label

            has_module_perms = model_admin.has_module_permission(request)
            if not has_module_perms:
                continue

            perms = model_admin.get_model_perms(request)

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True not in perms.values():
                continue

            info = (app_label, model._meta.model_name)
            model_dict = {
                'name': capfirst(model._meta.verbose_name_plural),
                'object_name': model._meta.object_name,
                'perms': perms,
                'admin_url': None,
                'add_url': None,
            }
            if perms.get('change') or perms.get('view'):
                model_dict['view_only'] = not perms.get('change')
                try:
                    model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=self.name)
                except NoReverseMatch:
                    pass
            if perms.get('add'):
                try:
                    model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=self.name)
                except NoReverseMatch:
                    pass

            if app_label in app_dict:
                app_dict[app_label]['models'].append(model_dict)
            else:
                app = apps.get_app_config(app_label)
                print(app.verbose_name,getattr(app,'icon',''))
                app_dict[app_label] = {
                    'name': app.verbose_name,
                    'app_label': app_label,
                    'app_icon': getattr(app,'icon',''),
                    'show_icon': getattr(settings,'SHOW_APP_ICON',False),
                    'app_url': reverse(
                        'admin:app_list',
                        kwargs={'app_label': app_label},
                        current_app=self.name,
                    ),
                    'has_module_perms': has_module_perms,
                    'models': [model_dict],
                }

        if label:
            return app_dict.get(label)
        return app_dict