from setuptools import setup, find_packages

VERSION = '0.2'

setup(name='pyqalxapi',
    version=VERSION,
    description="API Python Wrapper",
    long_description="API Python Wrapper",
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    keywords='api wrapper',
    author='',
    author_email='',
    url='https://bitbucket.org/agiletekengineering/pyqalxapi',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests',
        ],
    setup_requires=[
        ],
    entry_points="""
    """,
    namespace_packages=[
        ],
    )
