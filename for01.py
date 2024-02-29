numeros = [5,-3,10,8,-2,15,7,-9,4,6]
pos=[]
neg=[]
contPos=0
contNeg=0



for x in range(10):
    if numeros[x] <=0:
      neg.append(numeros[x])
      contNeg+=1
      
    else:
        pos.append(numeros[x])
        contPos+=1
print(pos)

print(neg)

print(contPos)

print(contNeg)
        

