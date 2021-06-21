from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'number',
    version = '0.0.1',
    description = 'This is python package that contains all functions for number manipulation.',
    py_modules = ["number"],
    package_dir = {'':'src'},
    extras_require = {
        "dev":[
            "pytest >= 3.7",
            "check-manifest",
            "twine"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "Vaidhyanathan S M",
    author_email = "vaidhyanathan.sm@gmail.com",
    url = "https://github.com/smv1999/number"
)