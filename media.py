def calcular_media(a, b):
    if a < 0 or b < 0:
        raise ValueError("Os números devem ser positivos.")
    return (a + b) / 2