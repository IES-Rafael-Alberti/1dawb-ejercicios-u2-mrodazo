import pytest
from src.ej2_17 import esFloat

@pytest.mark.parametrize(
    "entrada, expected",
    [
        ('10000', True),
        ('mujer', False),
        ('25.500', True),
    ]
)
def test_esFloat_params(entrada, expected):
    assert esFloat (entrada) == expected