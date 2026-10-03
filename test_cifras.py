import unittest

import cesar
import vigenere
import monoalfabetica
import transposicao

TEXTOS = [
    "Ataque ao amanhecer!",
    "ATTACKATDAWN",
    "ação, coração e pão 123",
    "a",
    "",
]


class TestCesar(unittest.TestCase):
    def test_valor_conhecido(self):
        self.assertEqual(cesar.criptografar("Ataque ao amanhecer!", 3), "Dwdtxh dr dpdqkhfhu!")

    def test_ida_e_volta(self):
        for texto in TEXTOS:
            for chave in (0, 3, 13, 25, 26, -5, 100):
                cifrado = cesar.criptografar(texto, chave)
                self.assertEqual(cesar.decriptografar(cifrado, chave), texto)


class TestVigenere(unittest.TestCase):
    def test_valor_conhecido(self):
        self.assertEqual(vigenere.criptografar("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")

    def test_ida_e_volta(self):
        for texto in TEXTOS:
            for chave in ("LEMON", "a", "Chave"):
                cifrado = vigenere.criptografar(texto, chave)
                self.assertEqual(vigenere.decriptografar(cifrado, chave), texto)

    def test_chave_invalida(self):
        for chave in ("", "abc1", "çã"):
            with self.assertRaises(ValueError):
                vigenere.criptografar("teste", chave)


class TestMonoalfabetica(unittest.TestCase):
    CHAVE = "QWERTYUIOPASDFGHJKLZXCVBNM"

    def test_valor_conhecido(self):
        self.assertEqual(monoalfabetica.criptografar("Hello, World!", self.CHAVE), "Itssg, Vgksr!")

    def test_ida_e_volta(self):
        chaves = [self.CHAVE] + [monoalfabetica.gerar_chave() for _ in range(5)]
        for texto in TEXTOS:
            for chave in chaves:
                cifrado = monoalfabetica.criptografar(texto, chave)
                self.assertEqual(monoalfabetica.decriptografar(cifrado, chave), texto)

    def test_chave_gerada_e_valida(self):
        chave = monoalfabetica.gerar_chave()
        self.assertEqual(len(chave), 26)
        self.assertEqual(set(chave), set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    def test_chave_invalida(self):
        for chave in ("ABC", "A" * 26, ""):
            with self.assertRaises(ValueError):
                monoalfabetica.criptografar("teste", chave)


class TestRailFence(unittest.TestCase):
    def test_valor_conhecido(self):
        self.assertEqual(transposicao.criptografar("ATAQUEAOAMANHECER", 3), "AUAHRTQEOMNEEAAAC")

    def test_ida_e_volta(self):
        for texto in TEXTOS:
            for chave in (1, 2, 3, 5, 50):
                cifrado = transposicao.criptografar(texto, chave)
                self.assertEqual(transposicao.decriptografar(cifrado, chave), texto)

    def test_chave_1_nao_altera(self):
        self.assertEqual(transposicao.criptografar("teste", 1), "teste")

    def test_chave_invalida(self):
        for chave in (0, -1, "3"):
            with self.assertRaises(ValueError):
                transposicao.criptografar("teste", chave)


if __name__ == "__main__":
    unittest.main()