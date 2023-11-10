import pytest
from src.ej2_16 import perteneceGrupo

@pytest.mark.parametrize(
    "sexo, nombre, expected",
    [
        ('mujer', 'Zoe', 'B'),
        ('mujer', 'Ana', 'A'),
        ('hombre', 'Zacarias', 'A'),
        ('hombre', 'Bruno', 'B'),
    ]
)
def test_perteneceGrupo_params(sexo, nombre, expected):
    assert perteneceGrupo (sexo, nombre) == expected
