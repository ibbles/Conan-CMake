from conans import ConanFile, CMake

class LowLevelLibrary(ConanFile):
    name = "LowLevelLibrary"
    version = "0.1"
    generators = "cmake"

    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = "./installed"
        cmake.configure()
        cmake.build()
        cmake.install()


    def package(self):
        self.copy("*.hpp", src="installed/include", dst="include")
        self.copy("*.so*", src="installed/lib", dst="lib/linux")

    def package_info(self):
        self.cpp_info.libdirs = ["lib/linux"]
        self.cpp_info.libs = ["LowLevelLibrary"]
