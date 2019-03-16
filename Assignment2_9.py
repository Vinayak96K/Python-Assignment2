def NumLen(no):
	iCnt=0
	while(no!=0):
		no=no/10
		iCnt=iCnt+1
	return iCnt

no=input('Enter a number:')
print('Lenght is:'),
print(NumLen(no))
