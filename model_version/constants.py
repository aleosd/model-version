from contextvars import ContextVar

versioning_is_disabled: ContextVar[bool] = ContextVar('versioning_is_disabled', default=False)
