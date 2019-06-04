from __future__ import absolute_import
import os
import pkg_resources


from pcrglobwb.bmiPcrglobwb import BmiPCRGlobWB as PcrGlobWb

PcrGlobWb.__name__ = "PcrGlobWb"
PcrGlobWb.METADATA = os.path.abspath(
    pkg_resources.resource_filename("pymt_pcrglobwb", "data/PcrGlobWb")
)

__all__ = [
    "PcrGlobWb",
]
