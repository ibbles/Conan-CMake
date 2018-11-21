from conans import ConanFile, CMake

class HighLevelLibrary(ConanFile):
    name = "HighLevelLibrary"
    version = "0.1"
    requires = "LowLevelLibrary/0.1@martin/testing"
    generators = "cmake"
    exports_sources = "*"


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()


    def package_info(self):
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.libs = ["HighLevelLibrary"]