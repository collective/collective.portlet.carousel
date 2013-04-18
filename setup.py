from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='collective.portlet.carousel',
      version=version,
      description="Carousel for collective.panels",
      long_description="""Carousel for collective.panels""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='carousel panels',
      author='Bo Simonsen',
      author_email='bo@headnet.dk',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'collective.panels',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
