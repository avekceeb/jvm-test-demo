
from subprocess import Popen, PIPE
from time import sleep
from threading import Timer
from os import environ, path, getcwd
from sys import version_info

Env = {
    'root': path.abspath(getcwd()),  # or abspath of (__file__)
    'javahome': None,
    'java': None,
    'javac': None,
    'source': '1.7',
    'asmtools': path.join(path.abspath(getcwd()), 'lib', 'asmtools.jar')
}


_bin_path = environ.get('PATH') if environ.get('PATH') \
    else '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/sbin:/usr/local/bin'


def is_string(s):
    if version_info[0] == 2:  # python 2 unicode != string
        if isinstance(s, basestring):
            return True
    else:
        if isinstance(s, str):
            return True
    return False


if version_info[:2] >= (3, 3):
    from shutil import which

    def find_exe(cmd):
        return which(cmd, path=_bin_path)
else:

    def find_exe(cmd):
        for d in _bin_path.split(":"):
            p = path.join(d, cmd)
            if path.exists(p):
                return p
        return None


class Failed(BaseException):

    def __init__(self, msg):
        self.e = "%r" % msg

    def __str__(self):
        return self.e

    def __repr__(self):
        return self.e


class Timeout(BaseException):

    def __init__(self, msg):
        self.e = "%r" % msg

    def __str__(self):
        return self.e

    def __repr__(self):
        return self.e


# TODO: optionally provide ENV
def run(cmd, timeout=45):
    def kill_proc(pr, to):
        to["expired"] = True
        pr.kill()
    if isinstance(cmd, str):
        cmd = cmd.split()
    if not cmd:
        return 99, "No command provided!", "", False
    if not path.isabs(cmd[0]):
        cmd[0] = find_exe(cmd[0])
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
    timedout = {"expired": False}
    if timeout:
        timer = Timer(timeout, kill_proc, args=[proc, timedout])
        timer.start()
    else:
        timer = None
    # communicate() returns a tuple (stdout_data, stderr_data).
    # The data will be strings if streams were opened in text mode; otherwise, bytes.
    sout, serr = proc.communicate()
    if timer:
        timer.cancel()
    return proc.returncode, sout, serr, timedout["expired"]


# TODO: option to check patterns in error messages
def assert_ok(cmd, **kwargs):
    ret, out, err, to = run(cmd, **kwargs)
    if to:
        raise Timeout(cmd)  # + err ???
    if 0 != ret:
        raise Failed(cmd)
    o = out.decode('utf-8')
    o += err.decode('utf-8')
    if version_info[0] == 2:  # python 2 unicode != string
        if isinstance(o, unicode):
            return o.encode('ascii', 'ignore')
    return o
