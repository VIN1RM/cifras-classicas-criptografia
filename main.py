import cesar
import vigenere
import monoalfabetica
import transposicao


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_chave_cesar(criptografando):
    return ler_inteiro("Chave (número inteiro): ")


def ler_chave_vigenere(criptografando):
    return input("Chave (palavra só com letras): ").strip()


def ler_chave_mono(criptografando):
    if criptografando:
        chave = input("Chave (26 letras) ou ENTER para gerar uma aleatória: ").strip()
        if not chave:
            chave = monoalfabetica.gerar_chave()
            print(f"Chave gerada (guarde para decifrar): {chave}")
        return chave
    return input("Chave (26 letras): ").strip()


def ler_chave_rail(criptografando):
    return ler_inteiro("Chave (número de trilhos): ")


CIFRAS = {
    "1": ("Cifra de César", cesar, ler_chave_cesar),
    "2": ("Cifra de Vigenère", vigenere, ler_chave_vigenere),
    "3": ("Substituição Monoalfabética", monoalfabetica, ler_chave_mono),
    "4": ("Transposição Rail Fence", transposicao, ler_chave_rail),
}


def menu():
    print("\n=== CRIPTOGRAFIA CLÁSSICA ===")
    for numero, (nome, _, _) in CIFRAS.items():
        print(f"{numero} - {nome}")
    print("0 - Sair")
    return input("Escolha a cifra: ").strip()


def main():
    while True:
        opcao = menu()
        if opcao == "0":
            print("Até mais!")
            break
        if opcao not in CIFRAS:
            print("Opção inválida.")
            continue

        nome, modulo, ler_chave = CIFRAS[opcao]
        print(f"\n--- {nome} ---")
        acao = input("[C]riptografar ou [D]ecriptografar? ").strip().upper()
        if acao not in ("C", "D"):
            print("Opção inválida.")
            continue

        criptografando = acao == "C"
        texto = input("Texto: ")
        try:
            chave = ler_chave(criptografando)
            if criptografando:
                resultado = modulo.criptografar(texto, chave)
            else:
                resultado = modulo.decriptografar(texto, chave)
            print(f"\nResultado: {resultado}")
        except ValueError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()