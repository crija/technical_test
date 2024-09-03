import math

def fibonacci_sequence_number(x):
    n = x * x

    calculo_1 = (5 * n + 4)
    calculo_2 = (5 * n - 4)

    resultado_1 = math.sqrt(calculo_1)
    resultado_2 = math.sqrt(calculo_2)

    return resultado_1 % 1 == 0 or resultado_2 % 1 == 0

fibonacci_sequence_number(1)




