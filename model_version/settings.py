import typing as t

from django.conf import settings

DEFAULT_VERSION: t.Final[int] = getattr(settings, "DEFAULT_VERSION", 0)
