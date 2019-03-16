def DigitSum(no):
	iCnt=0
	while(no!=0):
		iCnt=iCnt+(no%10)
		no=no/10
	return iCnt

no=input('Enter a number:')
print('Sum of digits:'),
print(DigitSum(no))
