#Questão 5

def is_palindrome(str):
    ''' retorna se a string dada é um palíndromo '''

    str = str.lower().replace(" ", "")
    palindrome = True
    for i in range(int(len(str)/2)):
        if (str[i] != str[len(str)-1-i]):
            palindrome = False
            break
    return palindrome

