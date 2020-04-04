def primo (n):
    divisores = 0
    for div in range (1, n + 1):
        if n % div == 0:
            divisores += 1

    if divisores == 2:
        return  True
    else:
        return False


cont = 0

x= 1
while cont <= 100:
    x+= 1
    if primo (x): 
        print (x, end='-')
        cont += 1
