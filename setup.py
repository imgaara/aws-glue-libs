#!/usr/bin/env python

# This file is required so that the bin/run file is created
# during the Jenkins build. This is the file used to run the application.
import setuptools

setuptools.setup(name='butterfly-aws-glue-libs',
                 version='1.0',
                 packages=setuptools.find_packages(),
                 install_requires=[
                 ],
                 dependency_links=[
                 ],
),


