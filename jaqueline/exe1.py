number = input("Digite os números da lista (separe-os por vírgula, ex: 0,1,0,3,12): ")
lista = [int(x.strip()) for x in number.split(',')]
semZero = [x for x in lista if x != 0]
zeros = [x for x in lista if x == 0]
listaresultado = semZero + zeros
print("Lista com zeros no final:", listaresultado)