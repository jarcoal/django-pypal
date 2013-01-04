#config
from django.conf import settings
from django_pypal import APPLICATION_ID, SECURITY_PASSWORD, SECURITY_SIGNATURE, SECURITY_USER_ID

#resources
from pypal import AdaptivePaymentsResource, AdaptiveAccountsResource, InvoiceResource, PermissionsResource


class DjangoPyPalMixin(object):
	"""
	Injects the user settings into the resource.
	"""

	def __init__(self, user_id=SECURITY_USER_ID, security_password=SECURITY_PASSWORD, security_signature=SECURITY_SIGNATURE, application_id=APPLICATION_ID, debug=settings.DEBUG):
		super(DjangoPyPalMixin, self).__init__(user_id, security_password, security_signature, application_id, debug)

#
# Mix the resources with the settings mixin.
#

class AdaptivePaymentsResource(DjangoPyPalMixin, AdaptivePaymentsResource):
	pass

class AdaptiveAccountsResource(DjangoPyPalMixin, AdaptiveAccountsResource):
	pass

class InvoiceResource(DjangoPyPalMixin, InvoiceResource):
	pass

class PermissionsResource(DjangoPyPalMixin, PermissionsResource):
	pass