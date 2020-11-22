from pytest import fixture
from util import Env


@fixture(scope="module",
         params=('1.6', '1.7', '1.8'),
         ids=('target=1.6', 'target=1.7', 'target=1.8'))
def all_java_targets(request):
    Env['target'] = request.param
    return request.param
