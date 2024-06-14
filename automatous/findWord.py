# Cria um autômato finito determinístico (DFA) a a partir da expressão regular.
def build_dfa(pattern):
    M = len(pattern) # calcula o comprimento do padrão de expressão regular.
    dfa = [{} for _ in range(M)] # Cria uma lista de dicionários, com Mentradas. Cada dicionário representará um estado no DFA, e as chaves serão caracteres (símbolos) do alfabeto, enquanto os valores serão o próximo estado para o qual fazer a transição ao encontrar esse caractere.
    dfa[0][pattern[0]] = 1 # define a transição inicial no DFA. Afirma que a partir do estado inicial (índice 0 na dfalista), encontrar o primeiro caractere ( pattern[0]) do padrão levará ao estado 1.
# Iterando através do padrão.
    X = 0 # Esta variável será usada para rastrear o estado atual durante o processo de construção.
    for j in range(1, M): # Itera pelos caracteres padrão, começando do segundo caractere (índice 1) até o último caractere ( M - 1).
# Preenchendo a Tabela de Transição        
        for c in range(256):   # Itera todos os caracteres possíveis (representados por seus códigos ASCII de 0 a 255) no intervalo de um byte. Isso garante que o DFA possa lidar com qualquer caractere, não apenas aqueles no padrão específico.
            dfa[j][chr(c)] = dfa[X].get(chr(c), 0) # Para cada estado je caractere c, esta linha tenta encontrar uma transição do estado X(o estado atual) ao encontrar o caractere c.
        # Configurando a transição explícita
        dfa[j][pattern[j]] = j + 1  #Esta linha define explicitamente a transição para o caractere na posição atual ( j) no padrão. Afirma que encontrar esse caractere específico no estado jlevará ao próximo estado ( j + 1).
        X = dfa[X].get(pattern[j], 0) #  atualiza a Xvariável para o próximo estado com base no estado atual ( X) e no caractere na posição atual ( pattern[j]) no padrão. Segue a mesma lógica da etapa 4b, mas especificamente para o caractere padrão.

    return dfa # Por fim, a função retorna o AFD construído, representado como uma lista de dicionários, onde cada dicionário representa um estado e suas transições para todos os caracteres possíveis.


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
