cmake_minimum_required(VERSION 3.6.2)
project({project_name})

set({project_id}_VERSION_MAJOR 1)
set({project_id}_VERSION_MINOR 0)
set({project_id}_VERSION_BUILD 0)

set(CMAKE_MODULE_PATH "${{PROJECT_SOURCE_DIR}}/cmake")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${{CMAKE_BINARY_DIR}}/output/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${{CMAKE_BINARY_DIR}}/output/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${{CMAKE_BINARY_DIR}}/output/bin)

include_directories(include)
include_directories(SYSTEM dependencies/include)

configure_file(
    "${{PROJECT_SOURCE_DIR}}/include/version.h.in"
    "${{PROJECT_BINARY_DIR}}/version.h")
