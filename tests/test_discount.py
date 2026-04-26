import pytest
import sys
import os

# Agregamos la carpeta raíz al path para que Python encuentre la carpeta 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.calculator import add, multiply, divide

# --- CASO 1: EXITOSO (CAMINO FELIZ) ---
def test_add_success():
    """Verifica que la suma de dos números positivos funcione correctamente"""
    print("\n[EJECUTANDO] test_add_success...")
    resultado = add(10, 5)
    assert resultado == 15
    # Agregamos una verificación extra para estar seguros
    assert add(-1, 1) == 0

# --- CASO 2: ERROR (MANEJO DE EXCEPCIONES) ---
def test_divide_by_zero_error():
    """Verifica que el sistema lance un ValueError al intentar dividir por cero"""
    print("\n[EJECUTANDO] test_divide_by_zero_error...")
    # Con pytest.raises probamos que el código realmente "explote" donde debe
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        divide(10, 0)

# --- CASO 3: CASO BORDE (EDGE CASE) ---
def test_multiply_by_zero_edge_case():
    """Verifica el comportamiento con el elemento absorbente (0)"""
    print("\n[EJECUTANDO] test_multiply_by_zero_edge_case...")
    # El cero es un caso borde típico porque suele causar errores lógicos
    assert multiply(500, 0) == 0
    assert multiply(0, 0) == 0