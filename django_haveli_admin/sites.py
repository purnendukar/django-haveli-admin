from django.contrib.admin.sites  import AdminSite

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