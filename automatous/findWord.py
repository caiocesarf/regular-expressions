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

# Este trecho de código verifica se um determinado padrão pode ser inserido em um índice específico dentro de uma string de texto sem violar os limites das palavras alfanuméricas. Isso ajuda a manter a integridade das palavras existentes ao inserir novo conteúdo.
def is_word_boundary(text, index, pattern_length):
    if index > 0 and text[index - 1].isalnum():
        return False
    if index + pattern_length < len(text) and text[index + pattern_length].isalnum():
        return False
    return True


def search(text, pattern): # esta linha define uma função chamada searchque recebe dois argumentos: text: a string de texto a ser pesquisada (supostamente uma string). pattern: o padrão a ser pesquisado (considerado uma string que representa uma expressão regular).
    dfa = build_dfa(pattern) # esta linha chama a função build_dfa para construir um DFA com base no padrão de expressão regular fornecido. Este DFA será usado para determinar com eficiência se uma sequência de caracteres no texto corresponde ao padrão.
    M = len(pattern) # Esta linha calcula o comprimento da string do padrão e o armazena na variável M.
    N = len(text) # Esta linha calcula o comprimento da string de texto e o armazena na variável N.
    j = 0 # Esta linha inicializa uma variável jcom 0. Ela será usada para rastrear a posição atual na string de texto durante o processo de pesquisa.
    positions = [] # Esta linha inicializa uma lista vazia chamada positions. Esta lista eventualmente armazenará os índices iniciais de todas as ocorrências do padrão encontrado no texto.

# Iterando através do texto
    for i in range(N): # Este loop itera sobre cada caractere ( text[i]) na string de texto.
# Transição no DFA
        j = dfa[j].get(text[i], 0) 
# combinando o padrão
        if j == M:
# Verificando os limites do Word (opcional)
            if is_word_boundary(text, i - M + 1, M):
# Armazenando correspondências
                positions.append(i - M + 1)
# Redefinindo o estado do DFA
            j = 0
# Retornando resultados
    return positions # Finalmente, a função retorna a positionslista, que contém os índices iniciais de todas as ocorrências não sobrepostas do padrão encontrado na string de texto.


T = (
    "O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. "
    "Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais "
    "e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). "
    "Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico.")

pattern = "computador"
positions = search(T, pattern)

print(f"A palavra '{pattern}' ocorre nas posições: {positions}")
