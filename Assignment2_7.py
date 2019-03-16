def pattern3(no):
	i=1
	while(i<=no):
		j=1
		while(j<=no):
			print(j),
			print(' '),
			j=j+1
		i=i+1
		print('')
	return

no=input('Enter a number:')
pattern3(no)
