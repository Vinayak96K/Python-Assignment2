def pattern2(no):
	i=0
	while(i<no):
		j=i
		while(j<no):
			print('* '),
			j=j+1
		print('')
		i=i+1

no=input('Enter a number:')
pattern2(no)
