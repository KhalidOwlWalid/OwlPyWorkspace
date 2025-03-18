from setuptools import setup, find_packages

setup(
    name="my_custom_package",
    version="0.1",
    find_packages=find_packages(),
    include_package_data=True,
    install_requires=[]
)