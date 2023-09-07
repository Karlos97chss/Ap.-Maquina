###==============set=================###
setMeuConjunto = set()
setMeuConjunto.add('a')
setMeuConjunto.add('d')
setMeuConjunto.add('a')
print(setMeuConjunto)

lisMinhaLista = [1,1,1,1,1,1,1,2,2,21,3,4,51,23,1,2,4,5,8]
print(lisMinhaLista)
print(set(lisMinhaLista))
###===============================###

f = open('meuArquivo.txt','x')
f = open('meuArquivo.txt','a')
f.write('Minha primeira linha.\n')
f.write('Minha segunda linha.\nTerceira linha')
f.close()

f = open('meuArquivo.txt','r')
arqMeuArquivo = f.read()
print(arqMeuArquivo)
f.close()

###==============Exercícios=================###

#list2 = ['Carro', 'Abajur', 'Moto', 'Barco', 'Ferro de passar roupa', 2, 'Barco', 'moto']
#print(list2)
#print(set(list2))


#file = open('meuTestGravar.txt','x')
#file = open('meuTestGravar.txt','a')
#file.write('Carro', 'Abajur', 'Moto', 'Barco', 'Ferro de passar roupam', 2, 'Barco', 'moto')

#file.write('Carro')
#file.write('Abajur')
#file.write('Moto')
#file.write('Barco')
#file.write('Ferro de passar roupa')
#file.write('2')
#file.write('Barco')
#file.write('moto')
#file.write(set('Carro', 'Abajur', 'Moto', 'Barco', 'Ferro de passar roupam', 2, 'Barco', 'moto'))
#file.close()

#file = open('meuTestGravar.txt','r')
#gravou = file.read()
#print(gravou)
#file.close()


###=========================Comparação=============================###

a = 1 
b = 2
c = 3
print(a==b)
print (a == b and a == a) 
print (a == b or a == a)
print (a == a or a == a and a==c) 
print (a == a and a == a or a==c)
print (a == a and a == c or a==a)
print (a == c and (a == c or a==a))

###=========================Comparação 01=============================###

a = 1
b = 2
c = 3

if (a == b):
    print ("Primeiro teste é verdadeiro.")
if (a == b and a == a):
    print ("Segundo teste é verdadeiro.")
if (a == b or a == a):
    print ("Terceiro teste é verdadeiro.")
if (a == a or a == a and a==c):
    print ("Quarto teste é verdadeiro.")
if (a == a and a == a or a==c):
    print ("Quinto teste é verdadeiro.")
if (a == a and a == c or a==a):
    print ("Sexto teste é verdadeiro.")
if (a == c and (a == c or a==a)):
    print ("Sétimo teste é verdadeiro.")
print ("Saindo do IF.")

###=========================Comparação 02=============================###

a = 1
b = 2
c = 3

if (a == b):
    print ("Primeiro teste é verdadeiro.")
if (a == b and a == a):
    print ("Segundo teste é verdadeiro.")
if (a == b or a == a):
    print ("Terceiro teste é verdadeiro.")
elif (a == a or a == a and a==c):
    print ("Quarto teste é verdadeiro.")
if (a == a and a == a or a==c):
    print ("Quinto teste é verdadeiro.")
if (a == a and a == c or a==a):
    print ("Sexto teste é verdadeiro.")
if (a == c and (a == c or a==a)):
    print ("Sétimo teste é verdadeiro.")
print ("Saindo do IF.")

###=========================Exercícios 02=============================###

#a = input('Qual o Primeiro valor?')
#b = input('Qual o Segundo valor?')

#if (a == b):
#    print("1 e 2 são iguais")
#else:
#    print('Não são iguais')

###===============================FOR=========================================###

IstMinhaLista = [1,2,3,4,5,6,7,8,9,10]

for numero in IstMinhaLista:
    if(numero % 2 == 0 ):
        print(f'O numero {numero} é par.')
    else:
        print(f'O numero {numero} é ímpar.')


istMinhaLista = [(1,2),(3,4),(4,5),(5,6),(7,8)]

print(len(istMinhaLista))

for item in istMinhaLista:
    print(item)

print(len(istMinhaLista))

for a,b in istMinhaLista:
    print(f'Este é o primeiro item da tupla:{a} e o segundo é: {b}')
    
IstMinhaLista1 = [1,2,3]
IstMinhaLista2 = ['a','b','c']
IstMinhaLista3 = [100,200,300]

IstMinhaLista4 = list(zip(IstMinhaLista1,IstMinhaLista2,IstMinhaLista3))

print(IstMinhaLista4)

IstMinhaLista1 = [1,2,3]

print(1 in IstMinhaLista1)

IstMinhaLista1 = [1,2,3,4,5]

print(max(IstMinhaLista1))
print(min(IstMinhaLista1))

###===============================Exercícios 3=========================================###

n = int(input("Quantos números você deseja inserir na lista? "))
numeros = []

for i in range(n):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

print("A lista de números é:", numeros)

numeros.sort()
print("Lista ordenada em ordem crescente:", numeros)

if 10 in numeros:
    print("O número 10 está presente na lista.")
else:
    print("O número 10 não está presente na lista.")
