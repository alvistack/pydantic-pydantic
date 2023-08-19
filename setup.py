# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pydantic',
    version='2.3.0',
    description='Data validation using Python type hints',
    author_email='Samuel Colvin <s@muelcolvin.com>, Eric Jolibois <em.jolibois@gmail.com>, Hasan Ramezani <hasan.r67@gmail.com>, Adrian Garcia Badaracco <1755071+adriangb@users.noreply.github.com>, Terrence Dorsey <terry@pydantic.dev>, David Montague <david@pydantic.dev>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Framework :: Hypothesis',
        'Framework :: Pydantic',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'annotated-types>=0.4.0',
        'pydantic-core==2.6.3',
        'typing-extensions>=4.6.1',
    ],
    extras_require={
        'email': [
            'email-validator>=2.0.0',
        ],
    },
    packages=[
        'pydantic',
        'pydantic._internal',
        'pydantic.deprecated',
        'pydantic.v1',
    ],
)
