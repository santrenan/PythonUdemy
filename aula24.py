nome = "sanitty"
preco = 1000.95897643

# %s -> Interpolação de string
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)
# %x ou %X -> converte para hexadecimal 
print("O hexadecimal de %d é %04x" % (1500, 1500))
