from setuptools import setup, find_packages
import os

version = '1.1'

setup(name='arcs.gsi',
      version=version,
      description="Library to assist GSI authentication and certificate handling in python.",
      long_description=open(os.path.join("README")).read() + "\n" +
                       open(os.path.join("CHANGES")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Topic :: Security :: Cryptography",
        "Intended Audience :: Developers",
        "Topic :: System :: Distributed Computing",
        ],
      keywords='',
      author='Russell Sim',
      author_email='russell.sim@arcs.org.au',
      url='http://code.arcs.org.au/gitorious/arcs-gsi/arcs-gsi',
      download_url='http://code.arcs.org.au/pypi/',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir = {'': 'src'},
      namespace_packages=['arcs'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'M2Crypto',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
