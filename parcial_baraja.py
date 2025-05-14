# Representacion de una baraja de cartas con tuplas

valores = ['10', 'J', 'Q', 'K', 'A'] 
palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']

baraja = [
    (valor, palo)
    for palo in palos
    for valor in valores]
def poker(mano):
    valores_mano = [carta[0] for carta in mano]
    for valor in valores_mano:
        if valores_mano.count(valor) == 4:
            return True
    return False
print(baraja)