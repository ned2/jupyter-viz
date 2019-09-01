import os

from setuptools import setup, find_packages


# Package meta-data.
NAME = "melbcafes"
DESCRIPTION = "Exploring Melbourne Cafes"

# These can be set to None if you want to omit them
URL = "None"
AUTHOR = "Ned Letcher"
AUTHOR_EMAIL = "ned at nedned dot net"
LICENSE = "MIT license"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = None  # get this from __version__.py


# What packages are required for this module to be executed?
REQUIRED = ["dash>=0.40.0", "dash-bootstrap-components>=0.3.0", "click"]

# What packages are optional?
#EXTRAS = {"prod": ["mod_wsgi"]}
EXTRAS = {}

# get the absolute path to this file
here = os.path.abspath(os.path.dirname(__file__))


# Import the README and use it as the long-description.
# Note: this will only work if "README.md" is present in your MANIFEST.in file!
try:
    with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


# If VERSION not specified above, load the package"s __version__.py module as a
# dictionary.
about = {}
if not VERSION:
    with open(
        os.path.join(here, "src", "melbcafes", "__version__.py")
    ) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=about["__version__"],
    packages=find_packages("src"),
    package_dir={"": "src"},
)
