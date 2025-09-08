# gridiron_gpt/setup.py

from setuptools import setup, find_packages

setup(
    name="phred",
    version="0.1.0",
    packages=find_packages(include=["phred*", "gridiron_gpt*"]),
    entry_points={
        'console_scripts': [
            'gridiron=phred.cli.main:app',
        ],
    },
)
