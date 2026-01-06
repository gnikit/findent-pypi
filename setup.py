import os

from skbuild import setup

# Read version from file, same as in CMakeLists.txt
with open(os.path.join(os.getcwd(), "version.txt")) as f:
    version = f.read().strip()

setup(
    name="findent",
    version=version,
    description="findent: powerful Fortran formatter",
    python_requires=">=3.7",
    long_description=open(os.path.join(os.getcwd(), "doc/README.md")).read(),
    long_description_content_type="text/markdown",
    author="Willem Vermin",
    # author_email="wvermin@gmail.com",
    maintainer="Giannis Nikiteas",
    keywords="fortran, formatter, format converter, dependency generator",
    url="https://github.com/wvermin/findent",
    license="BSD-3-Clause",
    platforms="Posix, Windows",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Fortran",
        "Programming Language :: C++",
        "Topic :: Software Development",
        "Topic :: Text Processing",
    ],
    cmake_args=("-G", "Unix Makefiles"),
)
