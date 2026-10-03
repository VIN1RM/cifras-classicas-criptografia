def _padrao_trilhos(tamanho, trilhos):
    """Retorna o trilho (0, 1, 2, 1, 0, ...) de cada posição do texto."""
    if trilhos == 1:
        return [0] * tamanho
    padrao = []
    trilho, passo = 0, 1
    for _ in range(tamanho):
        padrao.append(trilho)
        if trilho == 0:
            passo = 1
        elif trilho == trilhos - 1:
            passo = -1
        trilho += passo
    return padrao


def _validar_chave(chave):
    if not isinstance(chave, int) or chave < 1:
        raise ValueError("A chave deve ser um número inteiro maior ou igual a 1.")


def criptografar(texto, chave):
    _validar_chave(chave)
    padrao = _padrao_trilhos(len(texto), chave)
    linhas = [[] for _ in range(chave)]
    for caractere, trilho in zip(texto, padrao):
        linhas[trilho].append(caractere)
    return "".join("".join(linha) for linha in linhas)


def decriptografar(texto, chave):
    _validar_chave(chave)
    padrao = _padrao_trilhos(len(texto), chave)
    # posições do texto original, agrupadas por trilho (na ordem em que foram lidas)
    posicoes = sorted(range(len(texto)), key=lambda i: padrao[i])
    resultado = [""] * len(texto)
    for posicao, caractere in zip(posicoes, texto):
        resultado[posicao] = caractere
    return "".join(resultado)


if __name__ == "__main__":
    msg = "Vinícius Rodrigues Martins"
    chave = 3
    cifrado = criptografar(msg, chave)
    print("Cifrado:   ", cifrado)
    print("Decifrado: ", decriptografar(cifrado, chave))