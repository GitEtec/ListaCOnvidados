'''
Exercicio: Faça um programa que leia a quantidade de pessoas que serão convidadas,
Após isso  o mesmo ira perguntar quais é o nome de cada pessoa, seguidamente os itens sera adicionado em um lista, no final
a lista sera mostrada na tela.
'''


    
lista = []
i = 0    
q = int(input('Quantidade de convidados: '))
while i < q:
    n = str(input('Nome do convidado: '))
    lista.append(n)
    i +=1
print(lista)
