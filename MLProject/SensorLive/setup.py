from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str = "requirements.txt") -> List[str]:
    requirements = []

    try:
        with open(file_path) as f:
            requirements = f.read().splitlines()

        # remove editable install flag if present
        requirements = [req for req in requirements if req and req != "-e ."]

    except FileNotFoundError:
        print("requirements.txt not found — continuing without dependencies")

    return requirements


setup(
    name="SensorLive",
    version="0.1.0",
    packages=find_packages(),
    author="Omkar Nagargoje",
    author_email="imhere2k4@gmail.com",
    description="A Python package for real-time sensor data processing and visualization.",
    install_requires=get_requirements(),
)
