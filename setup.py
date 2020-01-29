from setuptools import setup

setup ( name='otctl',
  version='0.1',
  py_modules=['otctl_cli'],
  install_requires=[
      'Click',
      'PyYAML',
      'request',
  ],
  entry_points='''
    [console_scripts]
    otctl=otctl_cli:cli
    '''
)