from setuptools import setup, find_packages
from typing import List

hypne="-e."
def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]
        if hypne in requirements:
            requirements.remove(hypne)


    return requirements



setup(
    name="newml",
    version="0.1.0",
    packages=find_packages(),
    author="udhaya",
    author_email="udhayakumar1952004@gmail.com",
    install_requires=get_requirements("requirements.txt")


)