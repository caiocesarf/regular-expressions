import logging
import re

# Alfabetos
sigma = 'abcdefghijklmnopqrstuvwxyz'
gamma = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'

logging.basicConfig(level=logging.INFO)


# Expressão regular para Nome, nome do meio e sobrenome
def testar_nome(nomes):
    logging.info("Iniciando teste de Nomes")
    nome_regex = r'^[A-Z][a-z]*\s[A-Z]?[a-z]*\s?[A-Z][a-z]*$'
    for nome in nomes:
        if re.match(nome_regex, nome):
            print(f'O nome "{nome}" é válido de acordo com a expressão regular.')
        else:
            print(f'O nome "{nome}" não é válido de acordo com a expressão regular.')


# Expressão regular para E-mail
def testar_email(emails):
    logging.info("Iniciando teste de Email")
    email_regex = r'^[^@]+@[^@]+\.com\.br|\.br$'
    for email in emails:
        if re.match(email_regex, email):
            print(f'O e-mail "{email}" é válido de acordo com a expressão regular.')
        else:
            print(f'O e-mail "{email}" não é válido de acordo com a expressão regular.')


# Expressão regular para Senha
def testar_senha(senhas):
    logging.info("Iniciando teste de Senha")
    senha_regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z0-9]{8}$'
    for senha in senhas:
        if re.match(senha_regex, senha):
            print(f'A senha "{senha}" é válida de acordo com a expressão regular.')
        else:
            print(f'A senha "{senha}" não é válida de acordo com a expressão regular.')


# Expressão regular para CPF
def testar_cpf(cpfs):
    logging.info("Iniciando teste de CPF")
    cpf_regex = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    for cpf in cpfs:
        if re.match(cpf_regex, cpf):
            print(f'O CPF "{cpf}" é válido de acordo com a expressão regular.')
        else:
            print(f'O CPF "{cpf}" não é válido de acordo com a expressão regular.')


# Expressão regular para Telefone
def testar_telefone(telefones):
    logging.info("Iniciando teste de Telefones")

    telefone_regex = r'^(\(\d{2}\)\s?)?9\d{4}-\d{4}|\(\d{2}\)\s?9\d{8}|\d{2}\s?9\d{8}$'
    for telefone in telefones:
        if re.match(telefone_regex, telefone):
            print(f'O telefone "{telefone}" é válido de acordo com a expressão regular.')
        else:
            print(f'O telefone "{telefone}" não é válido de acordo com a expressão regular.')


# Expressão regular para Data e horário
def testar_data_horario(datas_horarios):
    logging.info("Iniciando teste de Datas e Horários")

    data_horario_regex = r'^\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}:\d{2}$'
    for data_horario in datas_horarios:
        if re.match(data_horario_regex, data_horario):
            print(f'A data e horário "{data_horario}" são válidos de acordo com a expressão regular.')
        else:
            print(f'A data e horário "{data_horario}" não são válidos de acordo com a expressão regular.')


# Expressão regular para Número real com ou sem sinal
def testar_numero_real(numeros_reais):
    logging.info("Iniciando teste de numeros reais")

    numero_real_regex = r'^[+-]?\d+\.\d+|^\d+$'
    for numero_real in numeros_reais:
        if re.match(numero_real_regex, numero_real):
            print(f'O número real "{numero_real}" é válido de acordo com a expressão regular.')
        else:
            print(f'O número real "{numero_real}" não é válido de acordo com a expressão regular.')


# Nomes Válidos
testar_nome(['Xavier Alexander Hawthorne', 'Ximena Aurora Hendricks', 'Xander Avery Hill', 'Xenia Beatrice Irwin',
             'Xochitl Bella Jacobs', 'Xenia Blair Jensen', 'Xavier Brooke Johnson', 'Xochitl Cassandra Jones',
             'Ximena Chloe Kelly', 'Xander Christopher Kennedy', 'Xandra Claire King', 'Xochitl Courtney Larson',
             'Ximena Danielle Lee', 'Xander David Lewis', 'Xenia Elizabeth Lopez', 'Xochitl Emily Martin',
             'Xavier Erica Martinez', 'Xandra Faye Matthews', 'Ximena Grace Miller', 'Xander Hannah Mitchell',
             'Xenia Holly Moore', 'Xochitl Isabella Murphy', 'Xavier Jasmine Nelson', 'Xandra Jessica Oliver',
             'Ximena Julia Parker', 'Xander Kathryn Patterson', 'Xenia Kelly Perez', 'Xochitl Lauren Peterson',
             'Xavier Madison Phillips', 'Xandra Michelle Pierce', 'Ximena Nicole Powell', 'Xander Olivia Price',
             'Xenia Penelope Quinn', 'Xochitl Rachel Ramirez', 'Xavier Samantha Reed', 'Xandra Sarah Reynolds',
             'Ximena Stephanie Richardson', 'Xander Taylor Roberts', 'Xenia Vanessa Robinson',
             'Xochitl Whitney Rodriguez', 'Xavier Zoe Russell', 'Xandra Ashley Sanders', 'Ximena Brianna Scott',
             'Xander Caitlin Shaw', 'Xenia Danielle Silva', 'Xochitl Emily Simmons', 'Xavier Erica Smith',
             'Xandra Faye Stevens', 'Ximena Grace Stewart', 'Xander Hannah Sullivan'])

# Nomes não válidos
testar_nome(['12345678 Hawthorne', 'Ximena 123 Aurora Hendricks', 'Xander 123 Avery Hill', 'Xenia 123 Beatrice Irwin',
             'Xochitl 123 Bella Jacobs', 'Xenia 123 Blair Jensen', 'Xavier 123 Brooke Johnson',
             'Xochitl 123 Cassandra Jones', 'Ximena 123 Chloe Kelly', 'Xander 123 Christopher Kennedy',
             'Xandra 123 Claire King', 'Xochitl 123 Courtney Larson', 'Ximena 123 Danielle Lee',
             'Xander 123 David Lewis', 'Xenia 123 Elizabeth Lopez', 'Xochitl 123 Emily Martin',
             'Xavier 123 Erica Martinez', 'Xandra 123 Faye Matthews', 'Ximena 123 Grace Miller',
             'Xander 123 Hannah Mitchell', 'Xenia 123 Holly Moore', 'Xochitl 123 Isabella Murphy',
             'Xavier 123 Jasmine Nelson', 'Xandra 123 Jessica Oliver', 'Ximena 123 Julia Parker',
             'Xander 123 Kathryn Patterson', 'Xenia 123 Kelly Perez', 'Xochitl 123 Lauren Peterson',
             'Xavier 123 Madison Phillips', 'Xandra 123 Michelle Pierce', 'Ximena 123 Nicole Powell',
             'Xander 123 Olivia Price', 'Xenia 123 Penelope Quinn', 'Xochitl 123 Rachel Ramirez',
             'Xavier 123 Samantha Reed', 'Xandra 123 Sarah Reynolds', 'Ximena 123 Stephanie Richardson',
             'Xander 123 Taylor Roberts', 'Xenia 123 Vanessa Robinson', 'Xochitl 123 Whitney Rodriguez',
             'Xavier 123 Zoe Russell', 'Xandra 123 Ashley Sanders', 'Ximena 123 Brianna Scott',
             'Xander 123 Caitlin Shaw', 'Xenia 123 Danielle Silva', 'Xochitl 123 Emily Simmons',
             'Xavier 123 Erica Smith', 'Xandra 123 Faye Stevens', 'Ximena 123 Grace Stewart',
             'Xander 123 Hannah Sullivan'])

# E-mail válidos
testar_email(['arthur.silva@exemplo.com.br', 'beatriz.araujo@exemplo.com.br', 'carlos.lima@exemplo.com.br',
              'diana.souza@exemplo.com.br', 'eduardo.pereira@exemplo.com.br', 'fernanda.oliveira@exemplo.com.br',
              'gustavo.costa@exemplo.com.br', 'helena.santos@exemplo.com.br', 'igor.martins@exemplo.com.br',
              'jessica.andrade@exemplo.com.br', 'kevin.silva@exemplo.com.br', 'lara.araujo@exemplo.com.br',
              'mateus.lima@exemplo.com.br', 'natalia.souza@exemplo.com.br', 'otavio.pereira@exemplo.com.br',
              'paloma.oliveira@exemplo.com.br', 'pedro.costa@exemplo.com.br', 'rafaela.santos@exemplo.com.br',
              'rodrigo.martins@exemplo.com.br', 'sabrina.andrade@exemplo.com.br', 'thiago.silva@exemplo.com.br',
              'vanessa.araujo@exemplo.com.br', 'walter.lima@exemplo.com.br', 'xenia.souza@exemplo.com.br',
              'yuri.pereira@exemplo.com.br', 'amanda.oliveira@exemplo.com.br', 'bruno.costa@exemplo.com.br',
              'clara.santos@exemplo.com.br', 'daniel.martins@exemplo.com.br', 'emily.andrade@exemplo.com.br',
              'fabio.silva@exemplo.com.br', 'gisele.araujo@exemplo.com.br', 'henrique.lima@exemplo.com.br',
              'isabella.souza@exemplo.com.br', 'joao.pereira@exemplo.com.br', 'karina.oliveira@exemplo.com.br',
              'lucas.costa@exemplo.com.br', 'maria.santos@exemplo.com.br', 'mateus.martins@exemplo.com.br',
              'nicole.andrade@exemplo.com.br', 'oliver.silva@exemplo.com.br', 'pamela.araujo@exemplo.com.br',
              'pedro.lima@exemplo.com.br', 'quezia.souza@exemplo.com.br', 'rafael.pereira@exemplo.com.br',
              'sarah.oliveira@exemplo.com.br', 'thomas.costa@exemplo.com.br', 'valentina.santos@exemplo.com.br',
              'victor.martins@exemplo.com.br', 'yasmin.andrade@exemplo.com.br'])

# E-mail não válidos
testar_email(['y0zb6p49@domain', '0mxhd958@.com.br', 'pxufvsaq@domain', '@wykmp0kh@mv9133uf.com.br', 'fq6go62o@.com.br',
              'HKPKER5Z@domain.com.br', '8s495xlu@.com.br', 'zdciubzu@domain', '@ib68xffp@tivbom9w.com.br',
              'ucbviy7e@.com.br', '173DYTAG@domain.com.br', 'uojfksq8@.com.br', 'ab52ej6z!@domain.com.br',
              '5yyc18qa@domain', '001rxk9f@domain', 'xw7dgf73@.com.br', 'M3ZXLKN3@domain.com.br',
              'VVK7DXN6@domain.com.br', 'IG7SM34B@domain.com.br', '8wqda1w2!@domain.com.br', 'J9MM7RFS@domain.com.br',
              'ffxd5j34@domain', '2sqd405m@.com.br', 'j7ws0omh@domain', 'RM44KJXI@domain.com.br',
              'bjlqevdt!@domain.com.br', 'b75am98c!@domain.com.br', 'o4dhr7b2@domain', 'VUOJOOT0@domain.com.br',
              'kf8s9web!@domain.com.br', '1qmzyjpm@domain', 'wfv9lgr5@domain', '2gd6wpz3@domain', 'f1d27d8m@domain',
              'y4rbkk76@domain', 'w6k2bebl@domain', '@ywd0w63o@cot2603t.com.br', 'b4n09doh!@domain.com.br',
              'x3z35ups@domain', 'ueonn3rc@domain', '@hmt64yle@mmv7oqbn.com.br', 'o3fc7bxc!@domain.com.br',
              'XTV7QPPC@domain.com.br', 'dfib0tkz'])

# Senha válida
testar_senha(
    ['4Xz2Y3v', 'b6B2nH7', '8m2C4j', '3vH7A5', '6N4aG9', '9A8cG2', '7x5B3v', '1B9c4H', '5H3A8v', '2B7x9j', '8c1A6v',
     '4v3B9H', '6H2x5j', '9A7c8v', '1B5A3H', '3v7B6H', '5Hx9c2j', '2B1A5v', '4v9B8H', '6Hx7c5j', '9A5c4v', '1B3A7H',
     '3v5B2H', '5Hx9c6j', '2B7A1v', '4v1B8H', '6Hx5c3j', '9A3c6v', '1B9A5H', '3v7B4H', '5Hx2c7j', '2B5A9v', '4v3B6H',
     '6Hx1c8j', '9A9c7v', '1B7A2H', '3v5B1H', '5Hx4c9j', '2B3A6v', '4v1B5H', '6Hx3c7j', '9A1c8v', '1B9A7H', '3v7B2H',
     '5Hx6c5j', '2B5A4v', '4v3B3H', '6Hx7c6j', '9A5c9v'])

# Senha não válida
testar_senha(
    ['abcdefgh', 'ABCDEFGH', '12345678', 'a!@#$$%^&', 'PASSWORD', 'qwerty123', 'iloveyou', 'football1', '123456',
     'baseball', 'dragon', '1qaz2wsx', 'starwars', 'princess', 'monkey', '123456789', 'football', '1q2w3e4r',
     'password1', 'iloveyou123', 'admin', '123qwe', 'asdfgh', 'password1234', '1qazxsw2', 'abc123', 'letmein', 'qwerty',
     'trustno1', '1234', 'password', '1q2w3e', 'dragon123', 'football', '1234567', 'baseball', '1qaz', 'starwars123',
     'princess', 'monkey123', 'admin123'])

# cpf válidos
testar_cpf(['000.000.000-00', '001.001.001-01', '002.002.002-02', '003.003.003-03', '004.004.004-04', '005.005.005-05',
            '006.006.006-06', '007.007.007-07', '008.008.008-08', '009.009.009-09', '010.010.010-10', '011.011.011-11',
            '012.012.012-12', '013.013.013-13', '014.014.014-14', '015.015.015-15', '016.016.016-16', '017.017.017-17',
            '018.018.018-18', '019.019.019-19', '020.020.020-20', '021.021.021-21', '022.022.022-22', '023.023.023-23',
            '024.024.024-24', '025.025.025-25', '026.026.026-26', '027.027.027-27', '028.028.028-28', '029.029.029-29',
            '030.030.030-30', '031.031.031-31', '032.032.032-32', '033.033.033-33', '034.034.034-34', '035.035.035-35',
            '036.036.036-36', '037.037.037-37', '038.038.038-38', '039.039.039-39', '040.040.040-40', '041.041.041-41',
            '042.042.042-42', '043.043.043-43', '044.044.044-44', '045.045.045-45', '046.046.046-46', '047.047.047-47',
            '048.048.048-48', '049.049.049-49', '050.050.050-50'])

# cpf não válidos
testar_cpf(['a00.a00.a00-aa', 'b01.b01.b01-bb', 'c02.c02.c02-cc', 'd03.d03.d03-dd', 'e04.e04.e04-ee', 'f05.f05.f05-ff',
            'g06.g06.g06-gg', 'h07.h07.h07-hh', 'i08.i08.i08-ii', 'j09.j09.j09-jj', 'k10.k10.k10-kk', 'l11.l11.l11-ll',
            'm12.m12.m12-mm', 'n13.n13.n13-nn', 'o14.o14.o14-oo', 'p15.p15.p15-pp', 'q16.q16.q16-qq', 'r17.r17.r17-rr',
            's18.s18.s18-ss', 't19.t19.t19-tt', 'u20.u20.u20-uu', 'v21.v21.v21-vv', 'w22.w22.w22-ww', 'x23.x23.x23-xx',
            'y24.y24.y24-yy', 'z25.z25.z25-zz', 'A00.A00.A00-AA', 'B01.B01.B01-BB', 'C02.C02.C02-CC', 'D03.D03.D03-DD',
            'E04.E04.E04-EE', 'F05.F05.F05-FF', 'G06.G06.G06-GG', 'H07.H07.H07-HH', 'I08.I08.I08-II', 'J09.J09.J09-JJ',
            'K10.K10.K10-KK', 'L11.L11.L11-LL', 'M12.M12.M12-MM', 'N13.N13.N13-NN', 'O14.O14.O14-OO', 'P15.P15.P15-PP',
            'Q16.Q16.Q16-QQ', 'R17.R17.R17-RR', 'S18.S18.S18-SS', 'T19.T19.T19-TT', 'U20.U20.U20-UU', 'V21.V21.V21-VV',
            'W22.W22.W22-WW', 'X23.X23.X23-XX', 'Y24.Y24.Y24-YY', 'Z25.Z25.Z25-ZZ'])

# telefone válido
testar_telefone(
    ['(11) 98765-4321', '(12) 99876-5432', '(13) 9876543210', '(14) 9765432100', '(15) 9654321000', '(16) 9543210000',
     '(17) 9432100000', '(18) 9321000000', '(19) 9210000000', '(21) 9100000000', '(22) 98765-4321', '(23) 99876-5432',
     '(24) 9876543210', '(25) 9765432100', '(26) 9654321000', '(27) 9543210000', '(28) 9432100000', '(29) 9321000000',
     '(31) 9210000000', '(32) 98765-4321', '(33) 99876-5432', '(34) 9876543210', '(35) 9765432100', '(36) 9654321000',
     '(37) 9543210000', '(38) 9432100000', '(39) 9321000000', '(41) 9210000000', '(42) 98765-4321', '(43) 99876-5432',
     '(44) 9876543210', '(45) 9765432100', '(46) 9654321000', '(47) 9543210000', '(48) 9432100000', '(49) 9321000000',
     '(51) 9210000000', '(52) 98765-4321', '(53) 99876-5432', '(54) 9876543210', '(55) 9765432100', '(56) 9654321000',
     '(57) 9543210000', '(58) 9432100000', '(59) 9321000000', '(61) 9210000000', '(62) 98765-4321', '(63) 99876-5432',
     '(64) 9876543210', '(65) 9765432100', '(66) 9654321000', '(67) 9543210000', '(68) 9432100000', '(69) 9321000000',
     '(71) 9210000000'])

# telefone não válido
testar_telefone(['(11) 9A7654B3210', '(12) 98765B4321', '(13) 9987654322C', '(14) 9876543213D', '(15) 9765432114E',
                 '(16) 9654321015F', '(17) 9543210016G', '(18) 9432100017H', '(19) 9321000018I', '(21) 9210000019J',
                 '(22) 98765-4321', '(23) 99876-5432', '(24) 9876543220K', '(25) 9765432121L', '(26) 9654321022M',
                 '(27) 9543210023N', '(28) 9432100024O', '(29) 9321000025P', '(31) 9210000026Q', '(32) 98765-4321',
                 '(33) 99876-5432', '(34) 9876543227R', '(35) 9765432128S', '(36) 9654321029T', '(37) 9543210030U',
                 '(38) 9432100031V', '(39) 9321000032W', '(41) 9210000033X', '(42) 98765-4321', '(43) 99876-5432',
                 '(44) 9876543234Y', '(45) 9765432135Z', '(46) 9654321036a', '(47)'])

# data e horário válido
testar_data_horario(
    ['25/12/2023 10:15:30', '01/01/1999 00:00:00', '31/10/2024 23:59:59', '08/05/2024 16:29:34', '14/03/2024 18:42:21',
     '29/09/1998 12:34:56', '12/06/2024 07:19:23', '27/02/2025 21:56:10', '05/08/2023 06:28:39', '16/11/2024 13:01:45',
     '23/04/2024 09:32:58', '10/07/1997 15:43:21', '01/09/2024 20:54:32', '18/12/2023 08:05:43', '30/05/2025 14:16:54',
     '07/10/2024 22:27:05', '24/01/1998 11:38:16', '03/06/2024 05:49:27', '20/11/2023 19:00:38', '01/03/2025 15:11:49',
     '18/08/2024 23:22:59', '26/12/1999 10:33:10', '04/07/2024 04:54:21', '21/10/2023 18:05:32', '02/04/2025 14:16:43',
     '19/09/2024 22:28:54', '27/01/1998 11:39:15', '05/06/2024 05:49:26', '22/11/2023 19:01:37', '02/03/2025 15:12:48',
     '19/08/2024 23:23:00', '27/12/1999 10:34:11', '05/07/2024 04:55:22', '22/10/2023 18:06:33', '03/04/2025 14:17:44',
     '20/09/2024 22:29:55', '28/01/1998 11:39:16', '06/08/2024 23:58:07', '23/11/2023 18:59:38', '04/05/2025 14:18:45',
     '21/10/2024 22:30:56', '29/01/1999 11:38:17', '07/07/2024 05:56:23', '24/12/2023 19:58:39', '05/04/2025 14:19:46',
     '22/09/2024 22:31:57', '30/01/2000 11:37:18', '08/08/2024 23:59:08', '25/11/2023 18:58:38', '06/06/2025 14:20:47',
     '23/10/2024 22:32:58', '31/01/2001 11:36:19', '09/08/2024 23:59:09', '26/11/2023 18:57:37', '07/07/2025 14:21:48',
     '24/10/2024 22:33:59', '01/02/2002 11:35:20', '10/08/2024 23:59:10', '27/11/2023 18:56:36', '08/07/2025 14:22:49',
     '25/10/2024 22:34:00', '02/02/2003 11:34:21', '11/08/2024 23:59:11', '28/11/2023 18:55:35', '09/07/2025 14:23:50',
     '26/10/2024 22:35:01', '03/02/2004 11:33:22', '12/08/2024 23:59:12', '29/11/2023 18:54:34', '10/07/2025 14:24:51',
     '27/10/2024 22:36:02', '04/02/2005 11:32:23', '13/08/2024 23:59:13', '30/11/2023 18:53:33', '11/07/2025 14:25:52',
     '28/10/2024 22:37:03', '05/02/2006 11:31:24', '14/08/2024 23:59:14', '01/12/2023 18:52:32', '12/07/2025 14:26:53',
     '29/10/2024 22:38:04', '06/02/2007 11:30:25', '15/08/2024 23:59:15', '02/12/2023 18:51:31', '13/07/2025 14:27:54',
     '30/10/2024 22:39:05', '07/02/2008 11:29:26', '16/08/2024 23:59:16', '03/12/2023 18:50:30', '14/07/2025 14:28:55',
     '31/10/2024 22:40:06', '08/02/2009 11:28:27', '17/08/2024 23:59:17', '04/12/2023 18:49:29', '15/07/2025 14:29:56'
     ])

# data e horário não válido
testar_data_horario(
    ['15/13/2024 20:14:55', '31/02/2024 23:59:59', '2024/05/08 14:32:58', '08/05/202a 14:32:58', '08/05/2024 60:32:58',
     '25/12/2023 14:32:aa', '31/10/2024 23:59:60', '08/05/2024 -14:32:58', '14/03/2024 24:42:21', '29/09/1998 12:34:5a',
     '12/06/2024 07:19:2a', '27/02/2025 21:56:1a', '05/08/2023 06:28:3a', '16/11/2024 13:01:4a', '23/04/2024 09:32:5a',
     '10/07/1997 15:43:2a', '01/09/2024 20:54:3a', '18/12/2023 08:05:4a', '30/05/2025 14:16:5a', '07/10/2024 22:27:0a',
     '24/01/1998 11:38:1a', '03/06/2024 05:49:2a', '20/11/2023 19:00:3a', '01/03/2025 15:11:4a', '18/08/2024 23:22:5a',
     '26/12/1999 10:33:1a', '04/07/2024 04:54:2a', '21/10/2023 18:05:3a', '02/04/2025 14:16:4a', '19/09/2024 22:28:5a',
     '27/01/1998 11:39:1a', '05/06/2024 05:49:2a', '22/11/2023 19:01:3a', '02/03/2025 15:12:4a', '19/08/2024 23:23:0a',
     '27/12/1999 10:34:1a', '05/07/2024 04:55:2a', '22/10/2023 18:06:3a', '03/04/2025 14:17:4a', '20/09/2024 22:29:5a',
     '28/01/1998 11:39:1a', '06/08/2024 23:58:0a', '23/11/2023 18:59:3a', '04/05/2025 14:18:4a', '21/10/2024 22:30:5a',
     '29/01/1999 11:38:1a', '07/07/2024 05:56:2a', '24/12/2023 19:58:3a', '05/04/2025 14:19:4a', '22/09/2024 22:31:5a',
     '30/01/2000 11:37:1a', '08/08/2024 23:59:0a', '25/11/2023 18:58:3a', '06/06/2025 14:20:4a', '23/10/2024 22:32:5a',
     '31/01/2001 11:36:1a', '09/08/2024 23:59:0a', '26/11/2023 18:57:3a', '07/07/2025 14:21:4a', '24/10/2024 22:33:5a',
     '01/02/2002 11:35:1a', '10/08/2024 23:59:0a', '27/11/2023 18:56:3a', '08/07/2025 14:22:4a', '25/10/2024 22:34:0a',
     '02/02/2003 11:34:1a', '11/08/2024 23:59:0a'])

# número real com ou sem sinal válido
testar_numero_real(
    ['+23.45', '-17.89', '654', '0.12', '-321', '+100', '4.56', '+0.09', '-87', '5.321', '+234', '-10', '987', '0.78',
     '+123', '-456', '3.14', '+0.01', '-90', '6.543', '+2345', '-1234', '8765', '0.1', '+1000', '-500', '4.2', '+0.001',
     '-10000', '7.321', '+12345', '-6789', '98765', '0.0001', '+100000', '-50000', '4.567', '+0.00001', '-1000000',
     '8.76543', '+234567', '-123456', '9876543', '0.000001', '+10000000', '-50000000', '5.67891', '+0.0000001',
     '-1000000000', '+23456789', '-123456789', '987654321', '0.00000001', '+10000000000', '+16.101110111010101010',
     '-67891011101010101010', '27.10111011101010101010', '+0.00000000000010000000000', '-100000000000000000000000',
     '38.10111011101010101010', '+2345678910111010101000', '-12345678910111010101000', '49.10111011101010101010',
     '0.0000000000001000000000000', '+10000000000000000000000000', '-50000000000000000000000000',
     '50.10111011101010101010', '+0.00000000000010000000000000', '-1000000000000000000000000000',
     '61.10111011101010101010', '+234567891011101010100000', '-1234567891011101010100000', '72.10111011101010101010',
     '0.000000000000100000000000000', '+1000000000000000000000000000', '-5000000000000000000000000000',
     '83.10111011101010101010', '+0.0000000000001000000000000000', '-10000000000000000000000000000',
     '94.10111011101010101010', '+23456789101110101010000000', '-123456789101110101010000000',
     '105.10111011101010101010', '0.00000000000010000000000000000', '+100000000000000000000000000000',
     '-500000000000000000000000000000', '116.10111011101010101010', '+0.000000000000100000000000000000',
     '-10000000000000000000000000000000', '127.10111011101010101010', '+2345678910111010101000'])

# número real com ou sem sinal não válido
testar_numero_real(
    ['!23.45', 'a-12.0', '789b', '++.', '--.', '1234', '567', '890', '+10000', '-50000', '+1234.', '-567.', '890.',
     '+10000.', '-50000.', '+1234.ab', '-567.cd', '890.ef', '+10000.gh', '-50000.ij', '1234a', '567b', '890c', '10000d',
     '-50000e', '+1234.aa', '-567.bb', '890.cc', '+10000.dd', '-50000.ee', '1234aa', '567bb', '890cc', '+10000dd',
     '-50000ee', '1234aaa', '567bbb', '890ccc', '+10000ddd', '-50000eee', '1234aaaa', '567bbbb', '890cccc',
     '+10000dddd', '-50000eeee', '1234aaaaa', '567bbbbb', '890ccccc', '+10000ddddd', '-50000eeeee', '1234aaaaaa',
     '567bbbbbb', '890cccccc', '+10000dddddd', '-50000eeeeee', '1234aaaaaaa', '567bbbbbbb', '890ccccccc',
     '+10000ddddddd', '-50000eeeeeee', '1234aaaaaaaa', '567bbbbbbbb', '890cccccccc', '+10000dddddddd', '-50000eeeeeee',
     '1234aaaaaaaaa', '567bbbbbbbbb', '890ccccccccc', '+10000ddddddddd', '-50000eeeeeeee', '1234aaaaaaaaaa',
     '567bbbbbbbbbb', '890cccccccccc', '+10000dddddddddd', '-50000eeeeeeeee', '1234aaaaaaaaaaa', '567bbbbbbbbbbb',
     '890cccccccccccc', '+10000ddddddddddd', '-50000eeeeeeeeee', '1234aaaaaaaaaaaa', '567bbbbbbbbbbbb',
     '890ccccccccccccc', '+10000dddddddddddd', '-50000eeeeeeeeeee', '1234aaaaaaaaaaaaa', '567bbbbbbbbbbbbb',
     '890cccccccccccccc', '+10000ddddddddddddd', '-50000eeeeeeeeeeee', '1234aaaaaaaaaaaaaa', '567bbbbbbbbbbbbbbb',
     '890ccccccccccccccc', '+10000dddddddddddddd', '-50000eeeeeeeeeeeeee', '1234aaaaaaaaaaaaaaa', '567bbbbbbbbbbbbbbbb',
     '-50000eeeeeeeeeeeeeeee', '1234aaaaaaaaaaaaaaaaaa', '567bbbbbbbbbbbbbbbbbbb', '890cccccccccccccccccccc',
     '+10000ddddddddddddddddddd', '-50000eeeeeeeeeeeeeeeeeee', '1234aaaaaaaaaaaaaaaaaaa', '567bbbbbbbbbbbbbbbbbbbb',
     '890ccccccccccccccccccccc', '+10000dddddddddddddddddddd', '-50000eeeeeeeeeeeeeeeeeeee', '1234aaaaaaaaaaaaaaaaaaaa',
     '567bbbbbbbbbbbbbbbbbbbb', '890cccccccccccccccccccccc', '+10000ddddddddddddddddddddd',
     '-50000eeeeeeeeeeeeeeeeeeee', '1234aaaaaaaaaaaaaaaaaaaaa', '567bbbbbbbbbbbbbbbbbbbb', '890ccccccccccccccccccccccc',
     '+10000dddddddddddddddddddddd', '-50000eeeeeeeeeeeeeeeeeeeeee', '1234aaaaaaaaaaaaaaaaaaaaaa',
     '567bbbbbbbbbbbbbbbbbbbb', '890cccccccccccccccccccccccc', '+10000ddddddddddddddddddddddd',
     '-50000eeeeeeeeeeeeeeeeeeeeeee', '1234aaaaaaaaaaaaaaaaaaaaaaa', '567bbbbbbbbbbbbbbbbbbbb',
     '890ccccccccccccccccccccccccc', '+10000dddddddddddddddddddddddd', '-50000eeeeeeeeeeeeeeeeeeeeeeeee',
     '1234aaaaaaaaaaaaaaaaaaaaaaaa'])
