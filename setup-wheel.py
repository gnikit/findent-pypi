import os
import setuptools

# Build specific variables should be overwritten by the build system
MAJOR_VERSION = 4
MINOR_VERSION = 1
PATCH_VERSION = 1

version = f"{MAJOR_VERSION}.{MINOR_VERSION}.{PATCH_VERSION}"
name = "findent"

################################################################################
FINDENT_ROOT = os.environ["FINDENT_ROOT"]
INSTALL_ROOT = os.environ["INSTALL_ROOT"]

print("VERSION: ", version)
print("FINDENT_ROOT: ", FINDENT_ROOT)
print("INSTALL_ROOT: ", INSTALL_ROOT)
################################################################################

# If built with Windows
if os.name == "nt":
    exes = [
        os.path.join(INSTALL_ROOT, "bin", "findent.exe"),
        os.path.join(INSTALL_ROOT, "bin", "wfindent"),
    ]
# POSIX OSs
else:
    exes = [
        os.path.join(INSTALL_ROOT, "bin", "findent"),
        os.path.join(INSTALL_ROOT, "bin", "wfindent"),
    ]


def gen_install_list(subdir):
    for dirpath, dirs, files in os.walk(subdir):
        if len(files) != 0:
            filepaths = [os.path.join(dirpath, f) for f in files]
            relpath = os.path.relpath(dirpath, INSTALL_ROOT)
            data_files.append((relpath, filepaths))


data_files = [("bin", exes)]
# gen_install_list(INSTALL_ROOT + "/share")

setuptools.setup(
    name=name,
    version=version,
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
    install_requires=["setuptools", "wheel"],
    data_files=data_files,
)
