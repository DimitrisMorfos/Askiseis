def maxSequence(lista):
    lilen=len(lista)
    max=0
    p=0
    a=0
    for i in range(0,lilen-1):
        for j in range(i+1,lilen):
            if sum(lista[i:j])>max:
                p=i
                a=j
                max=sum(lista[i:j])
    mlista=lista[p:a]
    return mlista
lista=input("Give a list:")
result=maxSequence(lista)
print sum(result),":",result
