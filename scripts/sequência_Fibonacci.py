import math

n = int(input('Digite um número qualquer: '))

r = n * n
calculo_1 = (5 * r + 4)
calculo_2 = (5 * r - 4)

resultado_1 = math.sqrt(calculo_1)
resultado_2 = math.sqrt(calculo_2)

print(resultado_1 % 1 == 0 or resultado_2 % 1 == 0)






