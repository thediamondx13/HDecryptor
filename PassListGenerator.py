import time
m = int(input('max num: '))
n = int(input('ammount of numbers: '))
f = open('wordlist.txt', 'w')
for i in range(m+1):
	i = str(i)
	if len(i) != n:
		for e in range(n-len(i)):
			i = '0' + i
	f.write(i+'\n')
	p = round(int(i)/m*100,1)
	print(f'{p}%')
f.close()
# thediamondx13
