import re

# Alfabeto
sigma = "HMhm"

# Expressões regulares
regex_a = r"M[H(hm)+]{2,}"
regex_b = r"M[H(hm)+]*[m(hm)+]*[m(hm)+]*$"
regex_c = r"M[H(hm)+]*[m(hm)+]*h$"
regex_d = r"(H[H(hm)+]*[m(hm)+]*){2,}"
regex_e = r"M[H(hm)+]*(h[m(hm)+]*)*"
regex_f = r"M[H(hm)+]*(h[m(hm)+]*){0,1}(h[m(hm)+]*){0,1}"
regex_g = r"M[H(hm)+]*(h[m(hm)+]*){0,2}"

# Testar as expressões regulares
def testar_arranjos(regex, descricao):
    print(f"\n{descricao}:")
    for arranjo in ["M", "MH", "Mhh", "Mhmm", "MHhm", "MHhmm", "MHhmhm", "MHhmhmh", "MHhmhmhm", "MHhmhmhmh"]:
        if re.match(regex, arranjo):
            print(f'O arranjo "{arranjo}" é válido de acordo com a expressão regular.')
        else:
            print(f'O arranjo "{arranjo}" não é válido de acordo com a expressão regular.')

testar_arranjos(regex_a, "Casais heterossexuais mais velhos que os filhos com pelo menos duas filhas mulheres, ou pelo menos um filho homem, ou ainda pelo menos dois filhos homens e uma filha mulher.")
testar_arranjos(regex_b, "Casais heterossexuais mais velhos que os filhos e com uma quantidade ímpar de filhas mulheres.")
testar_arranjos(regex_c, "Casais heterossexuais mais velhos que os filhos, com a filha mais velha mulher e o filho mais novo homem.")
testar_arranjos(regex_d, "Casais homossexuais mais velhos que os filhos, com pelo menos seis filhos, em que os dois primeiros filhos formam um casal e os últimos também.")
testar_arranjos(regex_e, "Casais homossexuais mais velhos que os filhos, em que o sexo dos filhos é alternado conforme a ordem de nascimento.")
testar_arranjos(regex_f, "Casais homossexuais mais velhos que os filhos, com qualquer quantidade de filhos homens e mulheres, mas que não tiveram dois filhos homens consecutivos.")
testar_arranjos(regex_g, "Arranjo de no mínimo x∈N e no máximo y∈N, com x>0,y>0, e x≤y, de adultos (Hs ou Ms) mais velhos que os filhos, com qualquer quantidade de filhos homens e mulheres, mas que os três filhos mais novos não foram homens.")
