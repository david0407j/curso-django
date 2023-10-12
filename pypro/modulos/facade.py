from typing import list

from pypro.modulo.modells import Modulo

def test_listar_modulos_ordenados() -> list[Modulo]:
    """
    lista de módulos ordenados por titulos
    :return:
    """
    return list(Modulo.objects.order_by('titulo').all())