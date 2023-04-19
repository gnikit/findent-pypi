cmake_minimum_required(VERSION 3.16 FATAL_ERROR)

project(findent LANGUAGES CXX)

# Force C++ 11 for all targets
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(ExternalProject)

# Set the default build type to Release
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Release" CACHE STRING "Choose the type of build." FORCE)
endif()

# Read the findent version from the version file
file(READ "${PROJECT_SOURCE_DIR}/version.txt" version)
message("version: ${version}")

set(FINDENT_TAG ${version} CACHE STRING "findent version to fetch and build")
set(WIN_FLAGS)
set(EXT)

if(WIN32)
  set(WIN_FLAGS --with-windows MINGW32=${CMAKE_CXX_COMPILER})
  set(EXT .exe)
  if (SKBUILD)
    # pip on Windows installs binaries to Scripts not bin
    message(STATUS "Will install binaries to Scripts")
    set(CMAKE_INSTALL_BINDIR Scripts)
  endif()
endif()

ExternalProject_Add(
  findent_src
  BINARY_DIR "${CMAKE_BINARY_DIR}/findent"
  URL "https://sourceforge.net/projects/findent/files/findent-${FINDENT_TAG}.tar.gz"
  SOURCE_DIR "${CMAKE_BINARY_DIR}/findent"
  CONFIGURE_COMMAND sh configure --prefix=${CMAKE_BINARY_DIR} ${WIN_FLAGS}
  BUILD_COMMAND make -j 2
  INSTALL_COMMAND make install
  DOWNLOAD_EXTRACT_TIMESTAMP true
)

# ExternalProject_Get_Property(findent_src binary_dir)
add_executable(findent_exe IMPORTED GLOBAL)
add_dependencies(findent_exe findent_src)
add_executable(wfindent_exe IMPORTED GLOBAL)
add_dependencies(wfindent_exe findent_src)

set_target_properties(findent_exe
  PROPERTIES
  IMPORTED_LOCATION ${CMAKE_BINARY_DIR}/bin/findent${EXT}
)

# set_target_properties(wfindent_exe
# PROPERTIES
# IMPORTED_LOCATION ${CMAKE_BINARY_DIR}/bin/wfindent
# )
install(IMPORTED_RUNTIME_ARTIFACTS findent_exe # wfindent_exe
  DESTINATION ${CMAKE_INSTALL_BINDIR}
)
