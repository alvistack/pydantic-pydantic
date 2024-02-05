# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pydantic',
    version='2.10.2',
    description='Data validation using Python type hints',
    author_email='Samuel Colvin <s@muelcolvin.com>, Eric Jolibois <em.jolibois@gmail.com>, Hasan Ramezani <hasan.r67@gmail.com>, Adrian Garcia Badaracco <1755071+adriangb@users.noreply.github.com>, Terrence Dorsey <terry@pydantic.dev>, David Montague <david@pydantic.dev>, Serge Matveenko <lig@countzero.co>, Marcelo Trylesinski <marcelotryle@gmail.com>, Sydney Runkle <sydneymarierunkle@gmail.com>, David Hewitt <mail@davidhewitt.io>, Alex Hall <alex.mojaki@gmail.com>, Victorien Plot <contact@vctrn.dev>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Hypothesis',
        'Framework :: Pydantic',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'annotated-types>=0.6.0',
        'pydantic-core==2.27.1',
        'typing-extensions>=4.12.2',
    ],
    extras_require={
        'email': [
            'email-validator>=2.0.0',
        ],
        'timezone': [
            'tzdata; python_version >= "3.9" and platform_system == "Windows"',
        ],
    },
    packages=[
        'pydantic',
        'pydantic._internal',
        'pydantic.deprecated',
        'pydantic.experimental',
        'pydantic.plugin',
        'pydantic.v1',
    ],
)
