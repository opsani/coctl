from setuptools import setup

setup ( name='coctl',
  version='0.2.1',
  py_modules=['coctl_cli'],
  install_requires=[
      'Click',
      'PyYAML',
      'requests',
  ],
  entry_points='''
    [console_scripts]
    coctl=coctl_cli:cli
    '''
)
