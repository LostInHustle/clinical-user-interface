"""Exception classes for invalid logout errors."""


class InvalidLogoutException(Exception):
    """Raised when a logout is attempted without being logged in."""
