# -*- coding: utf8 -*-
from setuptools import setup
from os import path

if __name__ == '__main__':
    setup(
        name='aiida',
        url='http://aiida.net/',
        license='MIT License',
        author='The AiiDA team',
        author_email='developers@aiida.net',
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
        ],
        version='0.8.0rc0',
        install_requires=[
            'aiida>=0.7.1'
        ],
        long_description=open(path.join(aiida_folder, 'README.rst')).read(),
    )
