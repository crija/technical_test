# bibliotéca para fazer a raiz quadrada
import math

# inserir o número no terminal
n = int(input('Digite um número qualquer: '))

# transformar em n2 para as fórmulas a seguir
r = n * n

# fórmulas usadas para saber se o número forma um quadrado perfeito
calculo_1 = (5 * r + 4)
calculo_2 = (5 * r - 4)

# calcular a raiz quadrada dos resultados das fórmulas
resultado_1 = math.sqrt(calculo_1)
resultado_2 = math.sqrt(calculo_2)

# fazer a divisão da raiz quadrada pra saber se o resultato é 0 e retornar True ou False
print(resultado_1 % 1 == 0 or resultado_2 % 1 == 0)






