q = 0.25
d = 0.10
n = 0.05
p = 0.01

def quantidade (valor):
    qtdq = 0
    qtdd = 0
    qtdn = 0
    qtdp = 0 
    
    result = valor // q    
    qtdq = qtdq + int(result)
    aux = float("%.2f" % (valor % q))
    if aux > 0:
        result = aux // d
        qtdd = qtdd + int(result)
        aux = float("%.2f" % (aux % d))
    if aux > 0:
        result = aux // n
        qtdn = qtdn + int(result)
        aux = float("%.2f" % (aux % n))
    if aux > 0:
        result = aux / p
        qtdp = qtdp + int(result)
    
    return f"{qtdq} quarters, {qtdd} dimes, {qtdn} nickels, {qtdp} pennies"    

def money():
    valor = float (input())    
    print(quantidade (valor))
money()