
a=int(input(" Дни: "))
f=float(input(" Процент увеличение на ден (цяло или дробно число): "))
c=float(input(" Сума (цяло или дробно число): "))
b=0

print("\n")
while b<a:
	b+=1
	if b%a==3:
		c=c-((f)/100)*c
	else:
		c=c+((f)/100)*c
	print(f" Ден {b}: {c:.2f} лв.")

