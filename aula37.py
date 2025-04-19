contador = 0

while contador < 30:
    contador += 1

    if contador == 6:
        print('"6" continue volta para o inicio do laço')
        continue

    if 10 <= contador <= 28:
        continue

    print(contador)
