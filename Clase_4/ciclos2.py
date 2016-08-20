lista = [1,2,3,4,5,6]

n = len(lista)

# range(comienzo, final, paso)
print "impares"
for i in range(0,n,2):  
	print lista[i]

print "pares"
for i in range(1,n,2):  
	print lista[i]


print "reves"
for i in range(n-1,-1,-1): 
	print lista[i]
