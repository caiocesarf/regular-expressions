def Aut_refri(aut,inicial,estados_finais, v):
    s = inicial #começa em q0
    print(s) #mostra estado inicial
    #para cada moeda no conjunto de moedas inseridas:
    for m in v:
        M = list(aut[s][m].values())[0] #carrega valor a ser impresso durante transição q0->qi dada a moeda a ser inserida
        s = list(aut[s][m].keys())[0] #transforma em estado atual o próximo estado ao qual o autômato foi conduzido mediante inserção da moeda
        print(M) #Realiza função de output do transdutor para valor de saída
        print(s) #Mostra o estado atual

    return s in estados_finais #retorna True se refrigerante pode ser retirado, False caso contrário.
    #Chama Função de testes de recebimento de moedas
valor1 = ["50", "25", "50", "100", "25", "50", "100"] # Teste do exemplo da questão
valor2 = ["50", "25", "50", "100"]
valor3 = ["100", "25"]
valor4 = ["25","25","25","25", "50","50", "100", "100", "25","50","25", "50","25","50", "50", "25"]
valor3 = ["50"]
valor5 = ["25", "25", "25", "100"]

#Autômato criado para o exercício
AR = {"q0": {'100': {"q4": 1} , '50':{"q2": 0} ,'25':{"q3": 0} },
            "q1": {'100': {"q7": 1} , '50':{"q5": 1} ,'25':{"q4": 1} },
            "q2": {'100': {"q6": 1} , '50':{"q4": 1} ,'25':{"q1": 0} },
            "q3": {'100': {"q5": 1} , '50':{"q1": 0} ,'25':{"q2": 0} },
            "q4": {'100': {"q4": 1} , '50':{"q2": 0} ,'25':{"q3": 0} },
            "q5": {'100': {"q5": 1} , '50':{"q1": 0} ,'25':{"q2": 0} },
            "q6": {'100': {"q6": 1} , '50':{"q4": 1} ,'25':{"q1": 0} },
            "q7": {'100': {"q7": 1} , '50':{"q5": 1} ,'25':{"q4": 1} },
            }

Aut_refri(AR, "q0", {"q4", "q5", "q6", "q7"}, valor1)
