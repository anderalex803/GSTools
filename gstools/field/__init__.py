# -*- coding: utf-8 -*-
"""
GStools subpackage providing tools for spatial random fields.

.. currentmodule:: gstools.field

Subpackages
^^^^^^^^^^^

.. autosummary::
    generator
    upscaling
    base

Spatial Random Field
^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   SRF
   Mesh

----
"""

from gstools.field.base import Mesh
from gstools.field.srf import SRF

__all__ = ["SRF", "Mesh"]
