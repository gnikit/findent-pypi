import os
import setuptools

# Build specific variables should be overwritten by the build system
MAJOR_VERSION = 4
MINOR_VERSION = 1
PATCH_VERSION = 1

# I assumed an insitu install, generated by ./configure --prefix=${PWD}/build/gnu && make install
# This prefix will have to change depending on the compiler used
# Easiest way I know is use a CI with 3 OSs, you then upload the *.whl files
# to PyPi
PREFIX = "build/gnu"
ROOT = os.path.dirname(os.path.abspath(__file__))
sdkdir = os.path.join(ROOT, PREFIX)
setupdir = os.path.join(ROOT, PREFIX)

version = f"{MAJOR_VERSION}.{MINOR_VERSION}.{PATCH_VERSION}"
name = "findent"


# If built with Windows
if os.name == "nt":
    exes = [
        os.path.join(setupdir, "bin", "findent.exe"),
        os.path.join(setupdir, "bin", "wfindent.exe"),
    ]
# POSIX OSs
else:
    exes = [
        os.path.join(setupdir, "bin", "findent"),
        os.path.join(setupdir, "bin", "wfindent"),
    ]


def gen_install_list(subdir):
    for dirpath, dirs, files in os.walk(subdir):
        if len(files) != 0:
            filepaths = [os.path.join(dirpath, f) for f in files]
            relpath = os.path.relpath(dirpath, setupdir)
            data_files.append((relpath, filepaths))


data_files = [("bin", exes)]
# gen_install_list(setupdir + "/share")

setuptools.setup(
    name=name,
    version=version,
    description="findent Fortran formatter test python wrapper",
    long_description=open(os.path.join(ROOT, "doc/README"), "r").read(),
    author="Willem Vermin",
    # author_email="wvermin@gmail.com",
    # maintainer="Ioannis Nikiteas",
    keywords="fortran, formatter",
    url="https://github.com/wvermin/findent",
    license="BSD License 2.0",
    platforms="Posix, Windows",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "BSD License v2",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Fortran",
        "Programming Language :: C++",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
    ],
    package_dir={"": os.path.join(ROOT + "/python")},
    data_files=data_files,
    
)
