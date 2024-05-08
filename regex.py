import logging
import re

# Alfabetos
sigma = 'abcdefghijklmnopqrstuvwxyz'
gamma = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'

# Expressão regular para Nome, nome do meio e sobrenome
def testar_nome(nomes):
    nome_regex = r'^[A-Z][a-z]*\s[A-Z]?[a-z]*\s?[A-Z][a-z]*$'
    for nome in nomes:
        if re.match(nome_regex, nome):
            print(f'O nome "{nome}" é válido de acordo com a expressão regular.')
        else:
            print(f'O nome "{nome}" não é válido de acordo com a expressão regular.')

# Expressão regular para E-mail
def testar_email(emails):
    email_regex = r'^[^@]+@[^@]+\.com\.br|\.br$'
    for email in emails:
        if re.match(email_regex, email):
            print(f'O e-mail "{email}" é válido de acordo com a expressão regular.')
        else:
            print(f'O e-mail "{email}" não é válido de acordo com a expressão regular.')

# Expressão regular para Senha
def testar_senha(senhas):
    senha_regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z0-9]{8}$'
    for senha in senhas:
        if re.match(senha_regex, senha):
            print(f'A senha "{senha}" é válida de acordo com a expressão regular.')
        else:
            print(f'A senha "{senha}" não é válida de acordo com a expressão regular.')

# Expressão regular para CPF
def testar_cpf(cpfs):
    cpf_regex = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    for cpf in cpfs:
        if re.match(cpf_regex, cpf):
            print(f'O CPF "{cpf}" é válido de acordo com a expressão regular.')
        else:
            print(f'O CPF "{cpf}" não é válido de acordo com a expressão regular.')

# Expressão regular para Telefone
def testar_telefone(telefones):
    telefone_regex = r'^(\(\d{2}\)\s?)?9\d{4}-\d{4}|\(\d{2}\)\s?9\d{8}|\d{2}\s?9\d{8}$'
    for telefone in telefones:
        if re.match(telefone_regex, telefone):
            print(f'O telefone "{telefone}" é válido de acordo com a expressão regular.')
        else:
            print(f'O telefone "{telefone}" não é válido de acordo com a expressão regular.')

# Expressão regular para Data e horário
def testar_data_horario(datas_horarios):
    data_horario_regex = r'^\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}:\d{2}$'
    for data_horario in datas_horarios:
        if re.match(data_horario_regex, data_horario):
            print(f'A data e horário "{data_horario}" são válidos de acordo com a expressão regular.')
        else:
            print(f'A data e horário "{data_horario}" não são válidos de acordo com a expressão regular.')

# Expressão regular para Número real com ou sem sinal
def testar_numero_real(numeros_reais):
    numero_real_regex = r'^[+-]?\d+\.\d+|^\d+$'
    for numero_real in numeros_reais:
        if re.match(numero_real_regex, numero_real):
            print(f'O número real "{numero_real}" é válido de acordo com a expressão regular.')
        else:
            print(f'O número real "{numero_real}" não é válido de acordo com a expressão regular.')


# Testar as expressões regulares
testar_nome(['Alan Turing', 'Ada Lovelace', 'Grace Hopper', 'Tim Berners-Lee', 'Stephen Cole Kleene', '1Alan', 'Alan',
             'A1an', 'A1an Turing', 'Alan turing'])

testar_email(['ada@lovelace.com.br', 'a@a.br', 'divulga@ufpa.br', 'a@a.com.br', '@', 'a@.br', '@a.br',
              'T@teste.br', 'a@A.com.br'])

testar_senha(['518R2r5e', 'F123456A', '1234567T', 'ropsSoq0', 'F1234567A', 'abcdefgH', '1234567HI'])

testar_cpf(['123.456.789-09', '987.654.321-00', '111.222.333-44', '123.456.789-09', '000.000.000-00', '123.456.789-0',
            '111.111.11-11'])

testar_telefone(['(91) 99999-9999', '99999-9999', '91 99999-9999', '(91) 99999-9999', '(91) 999999999', '91 999999999',
                 '(91) 59999-9999', '99 99999-9999', '(94)95555-5555'])

testar_data_horario(['31/08/2019 20:14:55', '01/01/2020 00:00:00', '29/02/2020 23:59:59', '31/08/2019 20:14:55',
                     '99/99/9999 23:59:59', '99/99/9999 3:9:9', '9/9/99 99:99:99', '99/99/999903:09:09'])

testar_numero_real(['-25.467', '3.1415', '0.0001', '-25.467', '1', '-1', '+1', '64.2', '1.', '.2', '+64,2'])