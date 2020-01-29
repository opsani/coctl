from setuptools import setup

setup ( name='coctl',
  version='0.1',
  py_modules=['coctl_cli'],
  install_requires=[
      'Click',
      'PyYAML',
      'request',
  ],
  entry_points='''
    [console_scripts]
    coctl=coctl_cli:cli
    '''
)
