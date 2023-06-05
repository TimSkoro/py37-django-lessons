from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MyPasswordValidator:
    """
    Validate that the password is not entirely numeric.
    """

    def validate(self, password, user=None):
        if "ru" in password:
            raise ValidationError(
                _("DNR_ERROR."),
                code="dnr_error",
            )

    def get_help_text(self):
        return _("HEllo py 37")
