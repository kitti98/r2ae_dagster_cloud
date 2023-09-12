from setuptools import find_packages, setup

setup(
    name="r2ae",
    install_requires=[
        "dagster",
        "dagster-cloud",
        "boto3",
        "pandas",
        "matplotlib",
    ],
    extras_require={"dev": ["dagster-webserver"]},
)
