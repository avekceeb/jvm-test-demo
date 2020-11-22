

## Demo Tests for JVM

#### How to Run

    # All the tests with default jdk:
    python3 -m pytest -v

    # Particular test
    python3 -m pytest -v -k test_get_static_bad_args

    # Group of tests:
    python3 -m pytest -v -m positive
    python3 -m pytest -v -m bytecode
    python3 -m pytest -v test_ddiv.py

    # Specify binaries to test:
    unset JAVA_HOME
    python3 -m pytest -v --javahome=/path-to-jdk

    # Specify binaries to test:
    python3 -m pytest -v --java=/path-to-java --javac=/path-to-javac

```
python3 -m pytest -v --java=/usr/lib/jvm/java-8-openjdk-amd64/bin/java --javac=/usr/bin/javac

Using java:  /usr/lib/jvm/java-8-openjdk-amd64/bin/java
Using javac: /usr/bin/javac

===================================================== test session starts =====================================================
platform linux -- Python 3.6.9, pytest-5.4.1, py-1.8.1, pluggy-0.13.1 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/dima/proj/java-vm-test, inifile: pytest.ini
collected 24 items                                                                                                            

test_ddiv.py::test_ddiv_sanity[target=1.6] PASSED                                                                       [  4%]
test_ddiv.py::test_ddiv_boundaries[target=1.6] PASSED                                                                   [  8%]
test_ddiv.py::test_ddiv_zero[target=1.6] PASSED                                                                         [ 12%]
test_ddiv.py::test_ddiv_nan[target=1.6] PASSED                                                                          [ 16%]
test_ddiv.py::test_ddiv_sanity[target=1.7] PASSED                                                                       [ 20%]
test_ddiv.py::test_ddiv_boundaries[target=1.7] PASSED                                                                   [ 25%]
test_ddiv.py::test_ddiv_zero[target=1.7] PASSED                                                                         [ 29%]
test_ddiv.py::test_ddiv_nan[target=1.7] PASSED                                                                          [ 33%]
test_ddiv.py::test_ddiv_sanity[target=1.8] PASSED                                                                       [ 37%]
test_ddiv.py::test_ddiv_boundaries[target=1.8] PASSED                                                                   [ 41%]
test_ddiv.py::test_ddiv_zero[target=1.8] PASSED                                                                         [ 45%]
test_ddiv.py::test_ddiv_nan[target=1.8] PASSED                                                                          [ 50%]
test_getstatic.py::test_sanity[target=1.6] PASSED                                                                       [ 54%]
test_getstatic.py::test_init_exception[target=1.6] PASSED                                                               [ 58%]
test_getstatic.py::test_big_const_pool[target=1.6] PASSED                                                               [ 62%]
test_getstatic.py::test_sanity[target=1.7] PASSED                                                                       [ 66%]
test_getstatic.py::test_init_exception[target=1.7] PASSED                                                               [ 70%]
test_getstatic.py::test_big_const_pool[target=1.7] PASSED                                                               [ 75%]
test_getstatic.py::test_sanity[target=1.8] PASSED                                                                       [ 79%]
test_getstatic.py::test_init_exception[target=1.8] PASSED                                                               [ 83%]
test_getstatic.py::test_big_const_pool[target=1.8] PASSED                                                               [ 87%]
test_getstatic.py::test_getstatic_interface PASSED                                                                      [ 91%]
test_getstatic.py::test_jasm_demo PASSED                                                                                [ 95%]
test_getstatic.py::test_get_static_bad_args PASSED                                                                      [100%]

===================================================== 24 passed in 8.59s ======================================================
```
