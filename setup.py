try:
    from setuptools import setup
    from setuptools.command import build_ext
except ImportError:
    from distutils.core import setup
    from distutils.command import build_ext

setup(
    name='connectable',
    version='0.1.0dev',
    author='Nicola Greco',
    author_email='notsecurity@gmail.com',
    packages=['connectable','connectable.test'],
    license='LICENSE.txt',
    long_description=open('README.md').read()
)