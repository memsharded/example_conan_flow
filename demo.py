#! /usr/bin/env python
import os


def run(cmd):
    print("\n%s\n" % cmd)
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Error running: %s" % cmd)


# This should work, but would pollute the current directory with temporary files
# run("conan source .")
# run("mkdir build")
# run("cd build && conan install ..")
# run('cd build && cmake ../hello"')
# run('cd build && cmake --build . --config Release')
# run('conan export-pkg . user/testing --build-folder=build')


run("conan source  . --source-folder=tmp/source")
run("conan install . --install-folder=tmp/install")
run("conan build   . --source-folder=tmp/source --install-folder=tmp/install --build-folder=tmp/build")
run("conan package . --source-folder=tmp/source --install-folder=tmp/install --build-folder=tmp/build --package-folder=tmp/package")
# NOTE: prevent ERROR: Package already exists
run("conan export-pkg . user/testing --source-folder=tmp/source --install-folder=tmp/install --build-folder=tmp/build --force")
# You can also test the package that was just exported
run("conan test test_package Hello/1.1@user/testing")

# Finally, run a full create, does all of the above + test_package
run('conan create . user/testing')
