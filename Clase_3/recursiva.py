def countdown(n):
	#Esta funcion se llama a si misma, es recursiva.
	if n <= 0:
		print "Despegue!!"
	else:
		print n
		countdown(n-1)

countdown(10)
