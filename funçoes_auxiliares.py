import random 
##-- função 1:  * há uma progressão que acompanha a funçao gera_num
x = 2
def gera_num(x):
    # x +=1
    return (random.randint(10**(x-1), (10**x)-1))
    
print (gera_num(x))

#ADICIONEI ALGO NOVO
