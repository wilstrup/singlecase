import os

from pathlib import Path
from setuptools import find_packages, setup

BUILD_NO = f".{os.environ['CI_PIPELINE_IID']}" if "CI_PIPELINE_IID" in os.environ else "+local"

with (Path(__file__).parent / "VERSION").open("r") as handle:
    BASE_VERSION = handle.readline().strip()

VERSION = BASE_VERSION + BUILD_NO


def get_requires():
    with open("requirements.txt") as f:
        requirements = []
        for requirement in f.read().splitlines():
            if requirement.startswith("# == Dev dependencies marker =="):
                break

            requirements.append(requirement)

        return requirements


setup(
    name="singlecase",
    version=VERSION,
    author="Abzu",
    description="Effect size estimation for single-case designs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=get_requires(),
    package_data={"": ["COMMIT_INFO"]},
)
