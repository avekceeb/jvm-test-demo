from os import remove, path
from shutil import rmtree
from pytest import mark, fixture, raises
from util_jdk import javac, java, jasm, jcoder
from util import Env, Failed
from tempfile import mkdtemp
from fixtures import all_java_targets


def setup_module(module):
    Env['sourcepath'] = path.join(Env['root'], 'java', 'jvmtest', 'getstatic')


def setup_function(function):
    Env['workdir'] = mkdtemp()


def teardown_function(function):
    rmtree(Env['workdir'])


@mark.positive
def test_sanity(all_java_targets):
    javac('TestSanity.java')
    java('getstatic.TestSanity')


@mark.positive
def test_init_exception(all_java_targets):
    javac('TestExceptionInInit.java')
    java('getstatic.TestExceptionInInit')


@mark.positive
def test_getstatic_interface():
    Env['source'] = '1.8'
    javac('TestInterface.java')
    java('getstatic.TestInterface')


@mark.positive
def test_big_const_pool(all_java_targets):
    javac('TestBigConstantPool.java', 'Bulk.java')
    java('getstatic.TestBigConstantPool')


@mark.bytecode
def test_jasm_demo():
    jasm("Demo.jasm")
    java("Demo")


@mark.bytecode
def test_get_static_bad_args():
    jcoder("WrongStaticDemo.jcod")
    with raises(Failed):
        java("WrongStaticDemo")
