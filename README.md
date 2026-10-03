# Universidade Evangélica de Goiás
# Engenharia de Software - Campus Anápolis
# 8º Período - Turma A - Noturno
# Disciplina: Segurança da Informação
# Discente: Vinícius Siqueira
# Discentes: 
# - Geovanna Teresa Félix - 2313275
# - Rafael França Martins - 2310947
# - Samuel Elias Morais Pereira - 2310544
# - Vinícius Rodrigues Martins - 2311066

# Atividade Cifras Clássicas em Python

Implementação autoral de quatro algoritmos históricos de criptografia, desenvolvida como atividade prática sobre os fundamentos da criptografia clássica.

| Cifra | Tipo | Chave | Arquivo |
|---|---|---|---|
| César | Substituição (deslocamento fixo) | número inteiro | `cesar.py` |
| Vigenère | Substituição polialfabética | palavra (apenas letras) | `vigenere.py` |
| Monoalfabética | Substituição (alfabeto embaralhado) | 26 letras sem repetição | `monoalfabetica.py` |
| Rail Fence | Transposição | número de trilhos | `transposicao.py` |

## Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa (usa apenas a biblioteca padrão)

## Como executar

Clone o repositório e rode o menu interativo:

```bash
git clone https://github.com/SEU_USUARIO/cifras-classicas.git
cd cifras-classicas
python main.py
```

O menu pergunta qual cifra usar, se você quer criptografar ou decriptografar, o texto e a chave.

Cada cifra também pode ser executada isoladamente para ver um exemplo:

```bash
python cesar.py
python vigenere.py
python monoalfabetica.py
python transposicao.py
```

## Como executar os testes

```bash
python -m unittest test_cifras.py -v
```

Os testes verificam, para cada cifra, um valor conhecido, a ida e volta (`decriptografar(criptografar(x)) == x`) e o tratamento de chaves inválidas.

## Estrutura do projeto

```
cifras-classicas/
├── cesar.py
├── vigenere.py
├── monoalfabetica.py
├── transposicao.py
├── main.py
├── test_cifras.py
└── README.md
```

Todas as cifras seguem a mesma interface:

```python
criptografar(texto, chave)    # retorna o texto cifrado
decriptografar(texto, chave)  # retorna o texto claro original
```

## Como cada cifra funciona

### 1. Cifra de César

Cada letra é deslocada N posições no alfabeto, onde N é a chave. Ao passar do Z, volta para o A.

- Criptografar: `(posição + chave) % 26`
- Decriptografar: `(posição - chave) % 26`

Exemplo com chave 3: `Ataque ao amanhecer!` vira `Dwdtxh dr dpdqkhfhu!`

Letras maiúsculas e minúsculas são preservadas. Espaços, números, acentos e pontuação permanecem inalterados.

### 2. Cifra de Vigenère

Variação do César em que a chave é uma palavra. Cada letra da chave define um deslocamento diferente, e a palavra se repete ao longo do texto.

```
Texto:  A  T  T  A  C  K  A  T  D  A  W  N
Chave:  L  E  M  O  N  L  E  M  O  N  L  E
Cifra:  L  X  F  O  P  V  E  F  R  N  H  R
```

Com a chave `LEMON`, `ATTACKATDAWN` vira `LXFOPVEFRNHR`. A chave só avança quando uma letra é cifrada, então espaços e pontuação não consomem a chave.

### 3. Substituição Monoalfabética

A chave é um alfabeto embaralhado com as 26 letras. Cada letra do alfabeto normal é trocada pela letra que ocupa a mesma posição na chave.

```
Normal: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Chave:  Q W E R T Y U I O P A S D F G H J K L Z X C V B N M
```

Com essa chave, `Hello, World!` vira `Itssg, Vgksr!`. Para decriptografar, os papéis do alfabeto e da chave são invertidos. A função `gerar_chave()` cria uma chave aleatória válida.

Existem 26! chaves possíveis, mas a cifra é vulnerável à análise de frequência, pois a distribuição das letras do idioma se mantém no texto cifrado.

### 4. Transposição Rail Fence

Nenhuma letra é trocada: apenas a posição delas muda. O texto é escrito em zigue-zague sobre N trilhos (a chave) e lido trilho por trilho.

Exemplo com 3 trilhos e o texto `ATAQUEAOAMANHECER`:

```
A . . . U . . . A . . . H . . . R
. T . Q . E . O . M . N . E . E .
. . A . . . A . . . A . . . C . .
```

Leitura por trilho: `AUAHR` + `TQEOMNEE` + `AAAC` = `AUAHRTQEOMNEEAAAC`

Nesta implementação, espaços e pontuação também são embaralhados, de modo que o texto decifrado volta idêntico ao original.

## Autor

Nome do grupo / integrantes: _preencher_