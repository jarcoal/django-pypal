from django.conf import settings

#
# Credentials
#

SECURITY_USER_ID = getattr(settings, 'PYPAL_SECURITY_USER_ID', None)
SECURITY_PASSWORD = getattr(settings, 'PYPAL_SECURITY_PASSWORD', None)
SECURITY_SIGNATURE = getattr(settings, 'PYPAL_SECURITY_SIGNATURE', None)

if settings.DEBUG:
	APPLICATION_ID = 'APP-80W284485P519543T'
else:
	APPLICATION_ID = getattr(settings, 'PYPAL_APPLICATION_ID', None)