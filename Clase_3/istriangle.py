def is_triangle(a,b,c):
	if a > b+c:
		print "No."
	elif b > a+c:
		print "No."
	elif c > a+b:
		print "No."
	else:
		print "Yes."
is_triangle(2,2,2)
is_triangle(6,2,2)
is_triangle(2,4,2)

