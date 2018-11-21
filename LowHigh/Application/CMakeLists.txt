project(Application)
cmake_minimum_required(VERSION 3.5)

include(${Application_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(Application main.cpp)

target_link_libraries(Application CONAN_PKG::HighLevelLibrary)
