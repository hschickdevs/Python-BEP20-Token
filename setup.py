from setuptools import setup, find_packages

import bep20


setup(
    name='bep20',
    version=bep20.__version__,
    author='Harrison Schick',
    author_email='hschickdevs@gmail.com',
    description='Python package that models the methods for tokens following the BEP-20 token standard on the Binance Smart chain.',
    url='https://github.com/hschickdevs/Python-BEP20-Token',
    # license='MIT',
    packages=['bep20'],
    include_package_data=True,
    install_requires=[line.strip() for line in open('requirements.txt').readlines()],
)