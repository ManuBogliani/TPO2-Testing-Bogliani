def calculate_discount(price, code):
    if price < 0:
        raise ValueError("El precio no puede ser negativo")
    
    discounts = {
        "PROMO10": 0.10,
        "BIENVENIDA20": 0.20,
        "SUPER50": 0.50
    }
    
    discount_rate = discounts.get(code, 0)
    return price * (1 - discount_rate)