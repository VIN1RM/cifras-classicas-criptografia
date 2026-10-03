def _deslocar(texto, chave):
    resultado = []
    for c in texto:
        if c.isalpha() and c.isascii():
            base = ord('A') if c.isupper() else ord('a')
            resultado.append(chr((ord(c) - base + chave) % 26 + base))
        else:
            resultado.append(c)  # espaços, números, acentos e pontuação ficam como estão
    return "".join(resultado)


def criptografar(texto, chave):
    return _deslocar(texto, chave)


def decriptografar(texto, chave):
    return _deslocar(texto, -chave)


if __name__ == "__main__":
    msg = "Samuel Elias Morais Pereira"
    chave = 3
    cifrado = criptografar(msg, chave)
    print("Cifrado:   ", cifrado)
    print("Decifrado: ", decriptografar(cifrado, chave))