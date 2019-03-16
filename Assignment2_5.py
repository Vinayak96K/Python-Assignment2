def chkPrime(no):
	if(no<0):
		no=-no
	i=(no/2)
	while(i>1):
		if((no%i)==0):
			break
		i=i-1
	if(i==1):
		print('Prime Number!')
	else:
		print('Not a Prime Number!')


no=input('Enter a number:')
chkPrime(no)
