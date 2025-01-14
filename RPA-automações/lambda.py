#Exemplo prático 1: Definição e uso
#Função regular

def dobrar(n):
   return n * 2

print('Função Regular:', dobrar(5)) # saída: 10

dobrar_com_lambda = lambda n: n * 2

print('Função Lambda:', dobrar_com_lambda(5))

def classificar_número(n):
  if n < 0:
    return 'Negativo'
  elif n == 0:
    return 'Zero'
  else:
    return 'Positivo'
print(classificar_número(-4))  

classificar_número_lambda = lambda n: 'Negativo' if n < 0 else( 'Zero' if n == 0 else 'Positivo')

print(classificar_número_lambda(0))

pessoas = [('João', 35), ('Maria', 25), ('Pedro', 40)]
pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])
print(pessoas_ordenadas)

# Filter com lambda

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)


numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero_ao_quadrado = list(map(lambda x: x ** 2, numero))

print(numero_ao_quadrado)

palavras = ['banana', 'abacate', 'arroz', 'feijão']

comprimentos = list(map(lambda palavra: len(palavra), palavras))

print(comprimentos)




