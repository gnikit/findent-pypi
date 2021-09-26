import os
import setuptools

# Build specific variables should be overwritten by the build system
MAJOR_VERSION = 4
MINOR_VERSION = 1
PATCH_VERSION = 1

version = f"{MAJOR_VERSION}.{MINOR_VERSION}.{PATCH_VERSION}"
name = "findent"

################################################################################
PREFIX = os.environ["OS_BUILD_PREFIX"]
PY_FILE = os.path.dirname(os.path.abspath(__file__))
FINDENT_ROOT = os.path.join(PY_FILE, f"{name}-{version}")  # XXX: to be removed
setupdir = os.path.join(FINDENT_ROOT, PREFIX)

print("VERSION: ", version)
print("FINDENT_ROOT: ", FINDENT_ROOT)
print("OS_BUILD_PREFIX: ", PREFIX)
print("SETUPDIR: ", setupdir)
################################################################################

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
    long_description=open(os.path.join(FINDENT_ROOT, "doc/README"), "r").read(),
    long_description_content_type="text/markdown",
    author="Willem Vermin",
    # author_email="wvermin@gmail.com",
    maintainer="Giannis Nikiteas",
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
        "Topic :: Scientific/Engineering",
    ],
    package_dir={"": os.path.join(PY_FILE + "/build")},
    data_files=data_files,
)
