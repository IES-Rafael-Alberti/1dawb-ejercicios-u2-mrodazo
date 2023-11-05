import pytest
from src.ej2_17 import comprobarNumeric, caracterLimitante, convertirAFloat, tipoImpositivo

@pytest.mark.parametrize(
    "entrada, expected",
    [
        ('10000', True),
        ('mujer', False),
        ('25.500', True),
        ('12.500,50', True),
    ]
)
def test_comprobarNumeric_params(entrada, expected):
    assert comprobarNumeric (entrada) == expected