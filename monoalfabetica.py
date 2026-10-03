import random
import string

ALFABETO = string.ascii_uppercase


def gerar_chave():
    letras = list(ALFABETO)
    random.shuffle(letras)
    return "".join(letras)


def _validar_chave(chave):
    if len(chave) != 26 or set(chave.upper()) != set(ALFABETO):
        raise ValueError("A chave deve ter as 26 letras de A a Z, sem repetir nenhuma.")


def _criar_tabela(origem, destino):
    origem, destino = origem.upper(), destino.upper()
    return str.maketrans(origem + origem.lower(), destino + destino.lower())


def criptografar(texto, chave):
    _validar_chave(chave)
    return texto.translate(_criar_tabela(ALFABETO, chave))


def decriptografar(texto, chave):
    _validar_chave(chave)
    return texto.translate(_criar_tabela(chave, ALFABETO))


if __name__ == "__main__":
    chave = "QWERTYUIOPASDFGHJKLZXCVBNM"
    msg = "Rafael França Martins"
    cifrado = criptografar(msg, chave)
    print("Chave:     ", chave)
    print("Cifrado:   ", cifrado)
    print("Decifrado: ", decriptografar(cifrado, chave))
    print("Chave aleatória de exemplo:", gerar_chave())