from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-nrrc',
    version=version,
    description="NRRC Portal",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Jessica Good',
    author_email='jessica.good@azgs.az.gov',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.nrrc'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        # myplugin=ckanext.nrrc.plugin:PluginClass
        # NRRC UI plugin.
	    nrrc_client=ckanext.nrrc.client.plugin:NRRCClient
    ''',
)