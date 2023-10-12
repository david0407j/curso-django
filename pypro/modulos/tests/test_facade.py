import pytest
from model_mommy import mommy
from pypro.modulos.models import Modulo
from pypro.modulos import facade


@pytest.fixture
def modulos(db):
    return [mommy.make(Modulo, titulo=s) for s in 'antes' 'depois'.split()]


def test_listar_modulos_ordenados(modulos):
    assert list(sorted(modulos, key= lambda modulo: modulo.titulo)) == facade.listar_modulos_ordenados()