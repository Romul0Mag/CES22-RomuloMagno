#Questão 4
import math

def is_prime(n):
    '''retorna se o numero dado é primo'''

    if(n<=1):
        prime = False
    else:
        lim = int(math.sqrt(n))
        prime = True

        # se n = 2 ou 3 temos range(2,2)(vazio), portanto não entra no loop e o resultado é True, ou seja, primo
        for i in range(2,lim + 1):
            if (n % (i) == 0):
                prime = False
                break
    return prime

