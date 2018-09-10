'''
Exercicio: Faça um programa que leia a quantidade de pessoas que serão convidadas,
Após isso  o mesmo ira perguntar quais é o nome de cada um.
Colocar os itens em uma lista apos isso ira imprimir todos os nomes da lista.
'''

#lista =[]
#q = int(input('Digite a quantidade de convidados: '))
#for i in range(0,q):
#    n = str(input('Nome do  convidado: '))
#    lista += n
#print(lista)
    
lista = []
i = 0    
q = int(input('Quantidade de convidados: '))
while i < q:
    n = str(input('Nome do convidado: '))
    lista.append(n)
    i +=1
print(lista)