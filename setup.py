from setuptools import setup, find_packages

setup(
    name="adtk",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
