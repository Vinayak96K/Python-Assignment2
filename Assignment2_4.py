def fun(no):
	sum=0
	i=1
	while(i<=(no/2)):
		if((no%i)==0):
			sum=sum+i
		i=i+1
	return sum

no=input('Enter a number:')
print('Sum of factors:'),
print(fun(no))
