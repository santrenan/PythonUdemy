a = 'Aaaa'
b = 'Bbbb'
c = 1.11111111
string = 'a={nome1} b={nome2} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c)

print(formato)
