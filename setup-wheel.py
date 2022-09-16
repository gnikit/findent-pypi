import glob
import os

import setuptools

name = "findent"

################################################################################
FINDENT_ROOT = os.environ["FINDENT_ROOT"]
INSTALL_ROOT = os.environ["INSTALL_ROOT"]
VERSION = os.environ["VERSION"]

print("VERSION: ", VERSION)
print("FINDENT_ROOT: ", FINDENT_ROOT)
print("INSTALL_ROOT: ", INSTALL_ROOT)
################################################################################

exes = glob.glob(os.path.join(INSTALL_ROOT, "bin/*"))
data_files = [("bin", exes)]

setuptools.setup(
    name=name,
    version=VERSION,
    description="findent: powerful Fortran formatter",
    long_description=open(os.path.join(os.getcwd(), "doc/README.md"), "r").read(),
    long_description_content_type="text/markdown",
    author="Willem Vermin",
    # author_email="wvermin@gmail.com",
    maintainer="Giannis Nikiteas",
    keywords="fortran, formatter, format converter, dependency generator",
    url="https://github.com/wvermin/findent",
    license="BSD License 2.0",
    platforms="Posix, Windows",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Fortran",
        "Programming Language :: C++",
        "Topic :: Software Development",
        "Topic :: Text Processing",
    ],
    package_dir={"": os.path.join(os.getcwd(), "build")},
    data_files=data_files,
)
