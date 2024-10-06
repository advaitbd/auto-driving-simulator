# setup.py

from setuptools import setup, find_packages

setup(
    name="auto-driving-simulator",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add any runtime dependencies here
    ],
)
