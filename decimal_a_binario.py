def decimal_a_binario(decimal):
    if decimal == 0:
        return '0'

    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2

    return binario

# Ejemplo de uso
print(decimal_a_binario(10))
