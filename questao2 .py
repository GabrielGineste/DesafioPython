"""
Exemplos:
    (){}([]), (), ()(), (({[]}))  <- Sim.
    ((), {{{)}], [][]]] <- Não.

Exemplo de Sim: {[]}
Exemplo de Não : (()
Exemplo de Não : ))
"""

# Código para testar
checar = "[][[]"
N = len(checar)


def testar_parenteses(st, N):

    resposta = True
    checar = []

    for i in st:

        if i == "(" or i == "[" or i == "{":
            checar.append(i)

        else:

            if len(checar) > 0:

                # Verifica se o topo da pilha é o par
                # do elemento atual.

                temp = checar[len(checar) - 1]
                checar.pop()

                if i == "(" and temp != ")":
                    resposta = False
                    break

                if i == "[" and temp != "]":
                    resposta = False
                    break

                if i == "{" and temp != "}":
                    resposta = False
                    break

            # se a pilha está vazia, NÃO

            else:
                resposta = False
                break
    
    # Se a pilha não estiver vazia depois
    # de ser transposta.

    if len(checar) > 0:
        resposta = False

    if resposta:
        print("SIM")
    else:
        print("NÃO")

testar_parenteses(checar, N)
