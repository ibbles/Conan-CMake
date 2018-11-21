project(HighLevelLibrary)
cmake_minimum_required(VERSION 3.5)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(HighLevelLibrary SHARED src/high_level_library.cpp)
target_include_directories(HighLevelLibrary PUBLIC include)
install(
    TARGETS HighLevelLibrary
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib)
install(
    DIRECTORY include/
    DESTINATION include
)