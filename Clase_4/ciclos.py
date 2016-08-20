"""En python hay varias maneras de hacer lo mismo,
 aprendelas todas y usalas como te convengan"""
 
lista = [1,2,3,4,5]
 
print "Para recorrer la lista usando el operador in y for:"
for i in lista:
	print i

#De la manera anterior no se usan indices pero tienes los valores

print "Usando un for y indices"

# La funcion range de python de vuelve el rango de 0 al numero dado.
# range(5) --> [0,1,2,3,4]
for i in range(len(lista)): 
	print "En el indice (posicion) ", i, "se encuentra el elemento ",lista[i]

# Ahora tienes indices y valores

print "Usando while y los indices"

n = len(lista)
i = 0
while i < n:
	print lista[i]
	i = i+1 #debo actualizar mi variable de iteracion
    
# Y finalmente en while tambien es posible.



