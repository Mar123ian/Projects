
a=int(input("Дни: "))
f=int(input("Десети от процента увеличение на ден: "))
b=0
c=50
g=" "
while b<a:
	b+=1
	if b%a==3:
		c=c-((f/10)/100)*c
	else:
		c=c+((f/10)/100)*c
	print(g+str(b)+g+str(c))

