import re

def check_family(family, regex):
  match = re.fullmatch(regex, family)
  return bool(match)

# a) Casais heterossexuais mais velhos que os filhos com pelo menos duas filhas mulheres,
# ou pelo menos um filho homem, ou ainda pelo menos dois filhos homens e uma filha mulher.
regex_a = r"(HM|MH)(mm|hh)(hh|m)"
print("a)", check_family("HMhhm", regex_a))  # True
print("a)", check_family("HMm", regex_a))    # False

# b) Casais heterossexuais mais velhos que os filhos e com uma quantidade ímpar de filhas
# mulheres.
regex_b = r"HMm(mm)*"
print("b)", check_family("HMmmm", regex_b))  # True
print("b)", check_family("HMmmmm", regex_b)) # False

# c) Casais heterossexuais mais velhos que os filhos, com a filha mais velha mulher e o filho
# mais novo homem.
regex_c = r"(HM|MH)(mh)(m/h)*"
print("c)", check_family("HMmh", regex_c))    # True
print("c)", check_family("HMhm", regex_c))    # False

# d) Casais homossexuais mais velhos que os filhos, com pelo menos seis filhos, em que os
# dois primeiros filhos formam um casal e os últimos também.
regex_d = r"HH(hh|mm){2,}(hh|mm)"
print("d)", check_family("HHhhhhhh", regex_d)) # True
print("d)", check_family("HHhhmmhh", regex_d))  # True
print("d)", check_family("HHhhmm", regex_d))    # False

# e) Casais homossexuais mais velhos que os filhos, em que o sexo dos filhos é alternado
# conforme a ordem de nascimento.
regex_e = r"HH(hm)+|(MM(mh)+)"
print("e)", check_family("HHhmhmhm", regex_e)) # True
print("e)", check_family("HHhmhmh", regex_e))  # False

# f) Casais homossexuais mais velhos que os filhos, com qualquer quantidade de filhos
# homens e mulheres, mas que não tiveram dois filhos homens consecutivos.
regex_f = r"HH(h?m)+|(MM(m?h)+)"
print("f)", check_family("HHhmhmhm", regex_f))   # True
print("f)", check_family("HHhhmhmh", regex_f))   # False


# g) Arranjo de no mínimo x∈IN e no máximo y∈IN, com x>0,y>0, e x≤y, de
# adultos (Hs ou Ms) mais velhos que os filhos, com qualquer quantidade de filhos
# homens e mulheres, mas que os três filhos mais novos não foram homens.
regex_g = r"(H+(?:[^H]*[HM]){3,}(?![^H]*HHH))"


# Testando com exemplos
print("g)", check_family("HHFFFH", regex_g))  # False
print("g)", check_family("MHMMMF", regex_g))  # True
print("g)", check_family("HHHFFF", regex_g))  # true