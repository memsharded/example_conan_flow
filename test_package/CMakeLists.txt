project(PackageTest CXX)
cmake_minimum_required(VERSION 3.1.2)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(example example.cpp)
conan_target_link_libraries(example)

# CTest is a testing tool that can be used to test your project.
enable_testing()
add_test(NAME example
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
         COMMAND example)
