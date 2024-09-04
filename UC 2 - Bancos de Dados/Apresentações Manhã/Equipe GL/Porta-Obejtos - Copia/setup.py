from setuptools import setup, find_packages

setup(
    name='portaobjetos',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'mysql-connector-python',
    ],
    entry_points={
        'console_scripts': [
            'portaobjetos=main:main',
        ],
    },
)
