"""Exception classes for duplicate login operations."""


class DuplicateLoginException(Exception):
    """Raised when a user attempts to log in while already logged in."""
