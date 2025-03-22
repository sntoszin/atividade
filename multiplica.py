
def multiplica_tudo(*args):
    produto = 1 
    for num     in args:
        produto *= num
    return produto


print(multiplica_tudo(5,6,7))