from os import path
from glob import glob
from util import assert_ok, Env


def javac(*sources):
    cmd = [
              Env['javac'],
              '-d', Env['workdir'],
              '-source', Env['target'],
              '-target', Env['target'],
          ] + [path.join(Env['sourcepath'], x) for x in sources]
    assert_ok(cmd)


def java(klass):
    cmd = [Env['java'], '-enableassertions', '-cp', Env['workdir'], klass]
    assert_ok(cmd)


def jasm(source):
    cmd = ['java',
           '-jar', Env['asmtools'],
           'jasm',
           '-d', Env['workdir'],
           path.join(Env['root'], 'jasm', source)]
    assert_ok(cmd)


def jcoder(source):
    cmd = ['java',
           '-jar', Env['asmtools'],
           'jcoder',
           '-d', Env['workdir'],
           path.join(Env['root'], 'jasm', source)]
    assert_ok(cmd)
