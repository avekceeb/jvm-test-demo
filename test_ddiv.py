from os import path
from shutil import rmtree
from pytest import mark, fixture, raises
from util import Failed, Env
from util_jdk import javac, java, jasm, jcoder
from tempfile import mkdtemp
from fixtures import all_java_targets


def setup_module(module):
    Env['sourcepath'] = path.join(Env['root'], 'java', 'jvmtest', 'ddiv')


def setup_function(function):
    Env['workdir'] = mkdtemp()


def teardown_function(function):
    rmtree(Env['workdir'])


def check_ddiv_present(classfile):
    return True


@mark.positive
def test_ddiv_sanity(all_java_targets):
    javac('TestSanity.java', 'Ddiv.java')
    java('ddiv.TestSanity')


@mark.positive
def test_ddiv_boundaries(all_java_targets):
    javac('TestBoundaries.java', 'Ddiv.java')
    java('ddiv.TestBoundaries')


@mark.positive
def test_ddiv_zero(all_java_targets):
    javac('TestZero.java', 'Ddiv.java')
    java('ddiv.TestZero')


@mark.positive
def test_ddiv_nan(all_java_targets):
    javac('TestNaN.java', 'Ddiv.java')
    java('ddiv.TestNaN')
