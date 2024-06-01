def build_dfa(pattern):
    M = len(pattern)
    dfa = [{} for _ in range(M)]
    dfa[0][pattern[0]] = 1

    X = 0
    for j in range(1, M):
        for c in range(256):
            dfa[j][chr(c)] = dfa[X].get(chr(c), 0)
        dfa[j][pattern[j]] = j + 1
        X = dfa[X].get(pattern[j], 0)

    return dfa


def is_word_boundary(text, index, pattern_length):
    if index > 0 and text[index - 1].isalnum():
        return False
    if index + pattern_length < len(text) and text[index + pattern_length].isalnum():
        return False
    return True


def search(text, pattern):
    dfa = build_dfa(pattern)
    M = len(pattern)
    N = len(text)
    j = 0
    positions = []

    for i in range(N):
        j = dfa[j].get(text[i], 0)
        if j == M:
            if is_word_boundary(text, i - M + 1, M):
                positions.append(i - M + 1)
            j = 0

    return positions


T = (
    "O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. "
    "Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais "
    "e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). "
    "Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico.")

pattern = "computador"
positions = search(T, pattern)

print(f"A palavra '{pattern}' ocorre nas posições: {positions}")