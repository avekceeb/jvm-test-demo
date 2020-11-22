
from os import path, environ
from util import Env, find_exe


def pytest_addoption(parser):
    for x in ('javahome', 'java', 'javac'):
        parser.addoption(
            '--%s' % x,
            dest='%s' % x,
            default=None,
            action="store"
        )


def pytest_configure(config):
    javahome = config.getoption('javahome')
    javahome = environ.get('JAVA_HOME') if (javahome is None) else javahome
    java = config.getoption('java')
    javac = config.getoption('javac')
    if javahome and path.exists(javahome):
        Env['java'] = path.join(javahome, 'bin', 'java')
        Env['javac'] = path.join(javahome, 'bin', 'javac')
        Env['javahome'] = javahome
    else:
        Env['javac'] = find_exe('javac') if (not javac) else javac
        Env['java'] = find_exe('java') if (not java) else java
    if (not Env['javac']) or (not path.exists(Env['javac'])):
        raise Exception('javac does not exists')
    if (not Env['java']) or (not path.exists(Env['java'])):
        raise Exception('java does not exists')
    print('')
    print(f"Using java:  {Env['java']}")
    print(f"Using javac: {Env['javac']}")
    print('')


def pytest_runtest_setup(item):
    pass


def pytest_exception_interact(node, call, report):
    pass


def pytest_runtest_teardown(item, nextitem):
    pass
