def es_balanceada(cadena):
    pila = []
    for caracter in cadena:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila:
                return False
            pila.pop()
    return len(pila) == 0
