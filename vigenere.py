def _validar_chave(chave):
    if not chave or not chave.isalpha() or not chave.isascii():
        raise ValueError("A chave deve conter apenas letras de A a Z.")


def _processar(texto, chave, sinal):
    _validar_chave(chave)
    deslocamentos = [ord(k) - ord('A') for k in chave.upper()]
    resultado = []
    i = 0  # só avança quando a gente cifra uma letra
    for c in texto:
        if c.isalpha() and c.isascii():
            base = ord('A') if c.isupper() else ord('a')
            d = deslocamentos[i % len(deslocamentos)] * sinal
            resultado.append(chr((ord(c) - base + d) % 26 + base))
            i += 1
        else:
            resultado.append(c)  # espaços, números e pontuação ficam como estão
    return "".join(resultado)


def criptografar(texto, chave):
    return _processar(texto, chave, 1)


def decriptografar(texto, chave):
    return _processar(texto, chave, -1)


if __name__ == "__main__":
    msg = "Geovanna Teresa Félix"
    chave = "LEMON"
    cifrado = criptografar(msg, chave)
    print("Cifrado:   ", cifrado)
    print("Decifrado: ", decriptografar(cifrado, chave))