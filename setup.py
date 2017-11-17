from setuptools import setup

setup(
    name='aloha',
    packages=['aloha'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-mysql'
    ],
)
