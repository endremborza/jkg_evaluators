import toml
import importlib
from setuptools import find_packages, setup

pytom = toml.load("pyproject.toml")
package_name = pytom["project"]["name"]
author_name = " - ".join(pytom["project"]["authors"][0]["name"])

mymodule = importlib.import_module(package_name)


with open("README.md") as fp:
    long_description = fp.read()

with open("requirements.txt") as fp:
    requirements = fp.read().strip().split()

if __name__ == "__main__":
    setup(
        name=package_name,
        version=mymodule.__version__,
        description=pytom["project"]["description"],
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="MIT",
        classifiers=["License :: OSI Approved :: MIT License"],
        url=pytom["project"]["urls"]["repository"],
        keywords=pytom["project"].get("keywords"),
        author=author_name,
        packages=find_packages(),
        include_package_data=True,
        python_requires=pytom["project"]["requires-python"],
        platforms="any",
        install_requires=requirements,
    )
