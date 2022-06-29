import pytest


@pytest.fixture(params=['a', 'b'], ids=['1', '2'], scope='session')
def qq(request):
    print(dir(request))
    print(f'{request.param=}')


def test_1(qq):
    print('test')

def test_2(qq):
    print('test')