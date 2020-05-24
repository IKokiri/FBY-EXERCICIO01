import queue
#Outras estruturas de dados
#1.1 Set Coleção não ordenada sem duplicidade
lista = [1,2,3,4,5,6,7,8,9]
print("####################################################")
print("1.1  Set Coleção não ordenada sem duplicidade")
print("####################################################")
print(set(lista))

#1.2 Tuple: Alguns valores separados por virgula
print("####################################################")
print("1.2 Tuple: Alguns valores separados por virgula")
print("####################################################")
tupla = (1,2,3,4,5,6,7,8,9)
print(tupla)

#2 Como usar listas
print("####################################################")
print("Como usar listas")
print("####################################################")
lista = queue.Queue()
print("entrou o numero 1")
lista.put(1)
print("entrou o numero 2")
lista.put(2)
print("entrou o numero 3")
lista.put(3)
print("entrou o numero 4")
lista.put(4)
print("entrou o numero 5")
lista.put(5)
print("entrou o numero 6")
lista.put(6)

print("Saiu o primeiro item da lista que é:")
print(lista.get())
print("Saiu o proximo item da lista que é:")
print(lista.get())
print("Saiu o proximo item da lista que é:")
print(lista.get())
print("Saiu o proximo item da lista que é:")
print(lista.get())
print("Saiu o proximo item da lista que é:")
print(lista.get())
print("Saiu o proximo item da lista que é:")
print(lista.get())

#2.1 Como uma fila (ou queue)
print("####################################################")
print("Como uma fila (ou queue)")
print("####################################################")
stack = []
print("entrou o numero 1")
stack.append('1')
print("entrou o numero 2")
stack.append('2')
print("entrou o numero 3")
stack.append('3')
print("entrou o numero 4")
stack.append('4')
print("entrou o numero 5")
stack.append('5')
print("entrou o numero 6")
stack.append('6')

print("Primeiro a sair da pilha")
print(stack.pop())
print("Proximo a sair da pilha")
print(stack.pop())
print("Proximo a sair da pilha")
print(stack.pop())
print("Proximo a sair da pilha")
print(stack.pop())
print("Proximo a sair da pilha")
print(stack.pop())
print("Proximo a sair da pilha")
print(stack.pop())

#3 O que o statement else faz em um loop (note que o 'else' está identado com o 'for')?
print("####################################################")
print("O que o statement else faz em um loop (note que o 'else' está identado com o 'for')?")
print("####################################################")

for n in range(2,10):
   for x in range(2,n):
       if n % x == 0:
           print(n,'equals', x, '*', n//x)
           break
   else:
       print(n, 'is a prime number') 

print("Isso acontece quando o for é executado é não é encontrada nehuma interrupção, neste caso o BREAK")