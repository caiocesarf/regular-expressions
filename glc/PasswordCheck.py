import re
import random
import string
import time
from pyparsing import Word, alphas, nums, oneOf, Combine, Suppress, StringEnd

# Função para validar senha usando expressões regulares
# A senha deve conter pelo menos uma letra maiúscula, um caractere especial e um número,
# além de ter no mínimo 8 caracteres.
def valida_senha_regex(senha):
    padrao = re.compile(r'^(?=.*[A-Z])(?=.*[a-zA-Z])(?=.*[!@#$%^&*(),.?":{}|<>])(?=.*\d).{8,}$')
    return bool(padrao.match(senha))

# Definição da Gramática Livre de Contexto (GLC) para senha
# Define regras para validar a estrutura da senha
letra_maiuscula = Word(alphas.upper(), exact=1)
letras = Word(alphas)
numeros = Word(nums)
especiais = oneOf("! @ # $ % ^ & * ( ) , . ? \" : { } | < >")
senha_glc = Combine(letra_maiuscula + letras + numeros + especiais + Word(alphas + nums + "!@#$%^&*(),.?\":{}|<>") + StringEnd())

# Função para validar senha usando GLC
def valida_senha_glc(senha):
    try:
        senha_glc.parseString(senha)
        return True
    except:
        return False

# Implementação do Autômato de Pilha
# O autômato armazena os diferentes tipos de caracteres da senha em uma pilha
class AutomatoPilha:
    def __init__(self):
        self.pilha = []

    # Processa cada caractere e o classifica conforme seu tipo
    def processar_caractere(self, caractere):
        if caractere.isupper():
            self.pilha.append('U')
        elif caractere.islower():
            self.pilha.append('L')
        elif caractere.isdigit():
            self.pilha.append('N')
        elif caractere in '!@#$%^&*(),.?\":{}|<>':
            self.pilha.append('S')

    # Valida se a senha atende aos critérios mínimos
    def validar_senha(self, senha):
        self.pilha = []
        for c in senha:
            self.processar_caractere(c)
        return 'U' in self.pilha and 'L' in self.pilha and 'N' in self.pilha and 'S' in self.pilha and len(senha) >= 8

# Função para gerar senhas aleatórias
def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*(),.?\":{}|<>"
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

# Gerando uma lista de 10.000 senhas para teste
senhas_teste = [gerar_senha(random.randint(8, 12)) for _ in range(10000)]

# Exibir as 10 primeiras senhas geradas e se são aceitas
print("Primeiras 10 senhas geradas e validação:")
for senha in senhas_teste[:10]:
    resultado = "Aceita" if valida_senha_regex(senha) else "Rejeitada"
    print(f"{senha}: {resultado}")

# Medindo tempo para Expressões Regulares
inicio_regex = time.perf_counter()
for senha in senhas_teste:
    valida_senha_regex(senha)
fim_regex = time.perf_counter()
tempo_regex = (fim_regex - inicio_regex) * 1000

# Medindo tempo para GLC
inicio_glc = time.perf_counter()
for senha in senhas_teste:
    valida_senha_glc(senha)
fim_glc = time.perf_counter()
tempo_glc = (fim_glc - inicio_glc) * 1000

# Medindo tempo para Autômato de Pilha
inicio_pilha = time.perf_counter()
for senha in senhas_teste:
    automato = AutomatoPilha()
    automato.validar_senha(senha)
fim_pilha = time.perf_counter()
tempo_pilha = (fim_pilha - inicio_pilha) * 1000

# Exibindo resultados
print("Tempo total de validação:")
print(f"Expressões Regulares: {tempo_regex:.2f} ms")
print(f"Gramática Livre de Contexto (GLC): {tempo_glc:.2f} ms")
print(f"Autômato de Pilha: {tempo_pilha:.2f} ms")

# Cálculo do tempo médio por senha
print("\nTempo médio por senha:")
print(f"Expressões Regulares: {tempo_regex / len(senhas_teste):.5f} ms")
print(f"Gramática Livre de Contexto (GLC): {tempo_glc / len(senhas_teste):.5f} ms")
print(f"Autômato de Pilha: {tempo_pilha / len(senhas_teste):.5f} ms")
