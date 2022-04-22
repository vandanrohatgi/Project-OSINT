from setuptools import find_packages
from setuptools import setup

setup(
    name="app",
    version="1.0.0",
    license="BSD",
    maintainer="vandanrohatgi",
    description="Project OSINT backend",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask","requests","flask_jwt_extended","flask_cors"],
    extras_require={"test": ["pytest", "pytest-flask","coverage"]},
)