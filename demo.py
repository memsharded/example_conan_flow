def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Error running: %s" % cmd)


run("conan source .")
run("mkdir build")
run("cd build && conan install ..")
run('cd build && cmake -G "Visual Studio 15 Win64"')
run('cd build && cmake --build . --config Release')