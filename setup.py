# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


readme = open('README.md').read()

setup(
    name='GroundTruth-Receiver',
    version='0.2.0',
    description=("A minimal server that will accept GroundTruth and store " +
                 "it in database"),
    long_description=readme,
    author='Romain Endelin',
    author_email='romain.endelin@mines-telecom.fr',
    url='https://github.com/pawmint/gt_receiver.git',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==0.10.1',
        'itsdangerous==0.24',
        'Jinja2==2.7.3',
        'MarkupSafe==0.23',
        'SQLAlchemy==0.9.9',
        'Flask-SQLAlchemy==2.0',
        'Werkzeug==0.10.1',
        'psycopg2==2.6',
        'Flask-Cors==1.10.3'
    ],
    license='Copyright',
    zip_safe=True,  # To be verified
    entry_points = {
        'console_scripts': ['gt_receiver=gt_receiver.server:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
        'License :: Other/Proprietary License',
        'Topic :: Scientific/Engineering'
    ],
)
