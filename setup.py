from setuptools import setup, find_packages


setup(
    name='pyhermes-server',
    version='0.1.0',
    description='Some custom utils for unittest2',
    long_description=open('README.rst').read(-1),
    author='Tomas Zulberti',
    author_email='tzulberti@gmail.com',
    license='BSD',
    url='https://github.com/tzulberti/pyhermes-server',
    install_requires=[
        "flask",
        "flask-sqlalchemy",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
