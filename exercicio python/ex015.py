km = float(input('Quantos kms o carro rodou? '))
dia = int(input('Por quantos dias o carro esteve alugado? '))
cust = (km * 0.15) + (dia * 60)
print('A estadia de {} dias e {} kms rodados custará R${:.2f}'.format(dia, km, cust))