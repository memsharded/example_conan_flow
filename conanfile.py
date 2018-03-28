from conans import ConanFile, CMake


class HelloConan(ConanFile):
    name = "Hello"
    version = "1.1"
    description = "Example of Conan Package Flow 1.1"
    license = "MIT"
    url = "https://bincrafters.github.io"
    #TBD settings = "os", "compiler", "build_type", "arch", "os_build", "arch_build"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/memsharded/hello.git")
        self.run("cd hello && git checkout static_shared")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="hello")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
