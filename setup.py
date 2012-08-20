from setuptools import setup, find_packages

VERSION = '0.0.1-dev'

LONG_DESCRIPTION = open('README.rst').read()

setup(name='dploy-app-service',
    version=VERSION,
    description="dploy-app-service",
    long_description=LONG_DESCRIPTION,
    keywords='git',
    author='Reuven V. Gonzales',
    author_email='reuven@tobetter.us',
    url="https://github.com/ravenac95/dploy-app-service",
    license='MIT',
    platforms='Ubuntu',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-mongokit',
        'flask-command',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'dploy-app-service = dployappservice.main:run',
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Build Tools',
    ],
)
