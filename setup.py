from setuptools import setup, find_packages
import os


setup(
    name='nessus',
    version='0.0.1',
    description='Python library to interface into Tenable\'s products and applications',
    author='Casey Reid',
    long_description="CLI for Nessus Pro",
    author_email='cyberdice113@gmail.com',
    url='none',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='nessus pro',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'arrow>=0.14.0',
        'Click>=7.0',
        'pprint>=0.1',
    ],
    extras_require={
    },
    entry_points={
        'console_scripts': [
            'nessus=nessus.cli:cli',
        ],
    },
)
