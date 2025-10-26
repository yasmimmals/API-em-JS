
num = input("Digite as listas (ex: 1,2; 5,5,0): ")
try:
    lista_de_listas = [
        [int(num.strip()) for num in sub_lista_str.split(',')]
        for sub_lista_str in num.split(';')
    ]
except:
    print("Entrada inválida. Certifique-se de usar o formato correto.")
    lista_de_listas = []
if lista_de_listas:
    lista_vencedora = max(lista_de_listas, key=sum)
    maior_soma = sum(lista_vencedora)

    print(f"\nLista Vencedora: {lista_vencedora}")
    print(f"Maior Soma: {maior_soma}")
else:
    print("Nenhuma lista válida para processar.")