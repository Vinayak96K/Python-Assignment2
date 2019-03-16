def fact(no):
	fact=1
	while(no!=1):
		fact=fact*no
		no=no-1
	return fact

no1=input('Enter a number')
print('Factorial:'),
print(fact(no1))
