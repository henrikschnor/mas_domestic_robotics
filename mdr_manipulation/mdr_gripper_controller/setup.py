#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['mdr_gripper_controller'],
    package_dir={'mdr_gripper_controller': 'ros/src/mdr_gripper_controller'}
)

setup(**d)
