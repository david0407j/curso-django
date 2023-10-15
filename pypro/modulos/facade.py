from typing import List

from pypro.modulos.models import Modulo

def test_listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista de módulos ordenados por titulos
    :return:
    """
    return list(Modulo.objects.order_by('titulo').all())