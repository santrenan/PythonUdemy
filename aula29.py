"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar


try: 
    pass
except:
    ...
"""

num_str = input("Dobra o número: ")

try: 
    print("String:", num_str)
    num_float = float(num_str) # ocorre um erro e pula para except
    print("Float:", num_float)
    print(f"O dobro de {num_str} é {num_float*2}")
except:
    print('Isso não é um número')