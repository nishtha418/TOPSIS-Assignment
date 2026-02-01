from setuptools import setup, find_packages

setup(
    name="Topsis-Nishtha-102303805",
    version="1.0.0",
    author="Nishtha",
    author_email="your_email@example.com",
    description="A Python package for TOPSIS multi-criteria decision making",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
)
