import pytest
from app.discount_manager import calculate_discount

# Caso 1: Exitoso
def test_calculate_discount_success():
    assert calculate_discount(100, "PROMO10") == 90.0
    assert calculate_discount(1000, "SUPER50") == 500.0

# Caso 2: Error (Excepción)
def test_calculate_discount_negative_price():
    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        calculate_discount(-10, "PROMO10")

# Caso 3: Caso Borde (Código inexistente o vacío)
def test_calculate_discount_invalid_code():
    # Si el código no existe, el precio debe mantenerse igual
    assert calculate_discount(100, "CODIGO_FALSO") == 100.0
    assert calculate_discount(100, "") == 100.0