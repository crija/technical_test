import math

def fibonacci_sequence_number(x):

    if x < 0: 
        return False

    n = x * x

    calculus_1 = (5 * n + 4)
    calculus_2 = (5 * n - 4)

    result_1 = math.sqrt(calculus_1)
    result_2 = math.sqrt(calculus_2)

    return result_1 % 1 == 0 or result_2 % 1 == 0

fibonacci_sequence_number(1)




