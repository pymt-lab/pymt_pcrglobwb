#! /usr/bin/env python
import os
import sys
import versioneer
from setuptools import find_packages, setup

from distutils.extension import Extension





packages = find_packages()
entry_points = {
    "pymt.plugins": [
        "PcrGlobWb=pymt_pcrglobwb.bmi:PcrGlobWb",
    ]
}

cmdclass = versioneer.get_cmdclass()

setup(
    name="pymt_pcrglobwb",
    author="Eric Hutton",
    description="PyMT plugin for pcrglobwb",
    version=versioneer.get_version(),
    packages=packages,
    cmdclass=cmdclass,
    entry_points=entry_points,
    include_package_data=True,
)
