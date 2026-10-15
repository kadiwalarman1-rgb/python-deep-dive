from setuptools import find_packages, setup


setup(
    name="ecommerce-system-lab34",
    version="1.0.0",
    description="Educational example of nested Python package organization",
    author="Python Deep Dive learner",
    packages=find_packages(),
    python_requires=">=3.9",
    extras_require={"http": ["requests>=2.31.0"]},
)
