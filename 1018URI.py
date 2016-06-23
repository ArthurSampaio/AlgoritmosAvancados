#coding: utf-8

valor1 = float(raw_input())
valor = int(valor1)
valor1 = int(valor1)

assert valor > 0 and valor < 1000000

cem = valor / 100
valor = valor % 100
cinquenta = valor / 50
valor = valor % 50
vinte = valor / 20
valor = valor % 20
dez = valor / 10
valor = valor % 10
cinco = valor / 5
valor = valor % 5
dois = valor / 2
valor = valor % 2
um = valor / 1

print valor1
print "%i nota(s) de R$ 100,00\n%i nota(s) de R$ 50,00\n%i nota(s) de R$ 20,00\n%i nota(s) de R$ 10,00\n%i nota(s) de R$ 5,00\n%i nota(s) de R$ 2,00\n%i nota(s) de R$ 1,00" %(cem, cinquenta, vinte, dez, cinco, dois, um)

