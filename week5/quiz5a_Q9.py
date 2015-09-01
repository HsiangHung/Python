# fibonacci number

length =40

fibonacci = [0,1]
index=1
#print range(length)

for i in range(length-1):
    #print index,fibonacci
    a1 = fibonacci[index-0]
    a2 = fibonacci[index-1]
    fibonacci.append(a2+a1)
    index = index+1
    

print fibonacci[len(fibonacci)-1]+fibonacci[len(fibonacci)-2]

