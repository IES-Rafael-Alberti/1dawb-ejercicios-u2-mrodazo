import pytest
from src.ej2_12a import comparaContrasena

@pytest.mark.parametrize(
    "passw1, passw2, expected",
    [
        ('lolo', 'Lolo', True),
        ('algo', 'nada', False),
        ('HOLA', 'hola', True),
        
    ]
)
def test_comparaContrasena_params(passw1, passw2, expected):
    assert comparaContrasena(passw1, passw2) == expected
