acoes = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


def compra_e_vende_acoes(precos):
    # Check if the precos array is less than 2
    if len(precos) < 2:
        return 0
        
    min_preco = precos[0]
    max_lucro = 0
    
    for preco in precos: 
       	min_preco = min(min_preco, preco)
        compare_lucro = preco - min_preco
        max_lucro = max(max_lucro, compare_lucro)
    
    return max_lucro

print(compra_e_vende_acoes(acoes))