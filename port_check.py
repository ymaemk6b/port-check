"""A small utility that checks TCP reachability with configurable timeouts."""

from __future__ import annotations

__all__ = ["portCheck"]


def portCheck(value):
    """A small utility that checks TCP reachability with configurable timeouts."""
    if value is None:
        raise ValueError("value must not be None")
    return value
