from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from .forms import AuthenticationForm
from .sites import HaveliAdminSite


class AdminAuthenticationForm(AuthenticationForm):

    """
    A custom authentication form used in the admin app.
    """
    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': _(
            "Please enter the correct %(username)s and password for a staff "
            "account. Note that both fields may be case-sensitive."
        ),
    }
    required_css_class = 'required'

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_staff:
            raise ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name}
            )

admin.site.__class__ = HaveliAdminSite
admin.site.login_form = AdminAuthenticationForm
# admin.site_header = "Django Haveli Admin"

