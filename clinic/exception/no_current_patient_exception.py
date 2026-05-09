"""Exception classes for no current patient errors."""


class NoCurrentPatientException(Exception):
    """Raised when an operation requires a current patient but none is set."""
