import setuptools
from distutils.core import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'FillingTimeSeries',    
  packages = ['FillingTimeSeries'], 
  version = '0.9.2',   
  license='MIT', # License from here: https://help.github.com/articles/licensing-a-repository
  description = 'Filling Time series: Package to fill missing values in geophysical time series in Python', # Short description
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = 'Rolando Jesus Duarte Mejias, Erick Rivera Fernandez',    
  author_email = 'rolando.duartemejias@ucr.ac.cr',
  url = 'https://github.com/rolandojduartem/FillingTimeSeries', # github or website
  download_url = 'https://github.com/rolandojduartem/FillingTimeSeries/archive/refs/tags/v_0_9_2.tar.gz', # Download file
  keywords = ['Time Series', 'Missing values', 'Metereology', "Geophysics", "Metereological"],
  setup_requires=['wheel'],
  install_requires=[       # I get to this in a second
          'statsmodels',
          'scikit-learn',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 4 - Beta', # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers', # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', # License
    'Programming Language :: Python :: 3', # Pyhton versions
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)