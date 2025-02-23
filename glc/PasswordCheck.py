import re
from pyparsing import Word, alphas, nums, oneOf, Combine, Suppress, StringEnd

# Função para validar senha usando expressões regulares
def valida_senha_regex(senha):
    # Expressão regular para verificar os critérios da senha:
    # (?=.*[A-Z])  -> Pelo menos uma letra maiúscula
    # (?=.*[a-zA-Z]) -> Pelo menos uma letra
    # (?=.*[!@#$%^&*(),.?":{}|<>]) -> Pelo menos um caractere especial
    # (?=.*\d) -> Pelo menos um número
    # .{6,} -> Pelo menos 6 caracteres no total

    padrao = re.compile(r'^(?=.*[A-Z])(?=.*[a-zA-Z])(?=.*[!@#$%^&*(),.?":{}|<>])(?=.*\d).{6,}$')
    return bool(padrao.match(senha))

# Definição da Gramática Livre de Contexto (GLC) para senha
# Uma senha válida deve conter:
# - Pelo menos uma letra maiúscula
# - Pelo menos uma letra qualquer
# - Pelo menos um número
# - Pelo menos um caractere especial
# - No mínimo 6 caracteres no total

letra_maiuscula = Word(alphas.upper(), exact=1)  # Uma letra maiúscula
letras = Word(alphas)  # Pelo menos uma letra
numeros = Word(nums)  # Pelo menos um número
especiais = oneOf("! @ # $ % ^ & * ( ) , . ? \" : { } | < >")  # Um caractere especial

# A senha deve começar com uma letra maiúscula, seguida de letras, números e caracteres especiais
senha_glc = Combine(letra_maiuscula + letras + numeros + especiais + Word(alphas + nums + "!@#$%^&*(),.?\":{}|<>") + StringEnd())

def valida_senha_glc(senha):
    try:
        senha_glc.parseString(senha)
        return True
    except:
        return False

# Testando as funções com exemplos de senha
senhas_teste = [
    "Aa1!abc",    # Válida
    "abcdef",     # Sem maiúscula, especial e número
    "Aaaaaa",     # Sem número e especial
    "123456",     # Sem letras
    "Aa!1",       # Muito curta
]

for senha in senhas_teste:
    print(f"Senha: {senha} | Regex: {valida_senha_regex(senha)} | GLC: {valida_senha_glc(senha)}")
