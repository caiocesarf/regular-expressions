import string

def is_word_boundary(text, index):
    if index < 0 or index >= len(text):
        return True
    return text[index] in string.whitespace + string.punctuation

def build_dfa(pattern):
    M = len(pattern)
    dfa = [{} for _ in range(M)]
    dfa[0][pattern[0]] = 1
    X = 0

    for j in range(1, M):
        for c in range(256):  # Considerando a tabela ASCII
            dfa[j][chr(c)] = dfa[X].get(chr(c), 0)
        dfa[j][pattern[j]] = j + 1
        X = dfa[X].get(pattern[j], 0)

    return dfa

def search_dfa(text, pattern):
    dfa = build_dfa(pattern)
    M = len(pattern)
    N = len(text)
    j = 0
    positions = []

    for i in range(N):
        j = dfa[j].get(text[i], 0)
        if j == M:
            start = i - M + 1
            end = i + 1
            if is_word_boundary(text, start - 1) and is_word_boundary(text, end):
                positions.append(start)
            j = 0  # Reset to start for next potential match

    return positions

# Texto fornecido
T = ("O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. "
     "Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais "
     "e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). "
     "Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico.")

# Palavra a ser buscada
pattern = "computador"

# Buscar ocorrências
positions = search_dfa(T, pattern)

# Exibir resultados
print("A palavra '{}' ocorre nas posições: {}".format(pattern, positions))