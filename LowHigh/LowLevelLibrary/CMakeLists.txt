project(LowLevelLibrary)
cmake_minimum_required(VERSION 3.5)

add_library(
    LowLevelLibrary SHARED
    src/low_level_library.cpp)

target_include_directories(
    LowLevelLibrary PUBLIC "include")

install(
    TARGETS LowLevelLibrary
    LIBRARY DESTINATION "lib"
    RUNTIME DESTINATION "bin")

install(
    DIRECTORY include/
    DESTINATION include)
