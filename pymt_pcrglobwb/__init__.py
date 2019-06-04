#! /usr/bin/env python

from .bmi import (PcrGlobWb,
)

__all__ = ["PcrGlobWb",
]

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
