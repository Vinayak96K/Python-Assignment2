def pattern1(no):
	i=0
	while(i<no):
		j=0
		while(j<no):
			print('* '),
			j=j+1
		i=i+1
		print('')
	return

#call the function
no1=input('Enter a number:')
pattern1(no1)
