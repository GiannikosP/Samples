import random
for k in range (1000):
	check=[]
	p=[]
	ncount=0
	allcount=0
	for i in range(100):
		print 'p',i+1,'turn'
		check.append(0)
		for j in range(5):
			new=[]
			c=0
			while True:
				newnum= int(raw_input("insert a number"))
				new.append(newnum)
				if new[-1] > 0 and new[-1] < 81:
				    c=1
				else: 
					print 'try again'
					
					
				if c == 1:
						print 'ok'
						p.append(new)
						break
	print 'please wait'					
	while True:
		numbr= random.randint(1,80)
		ncount +=1
		for i in range(1,101):
			
			for j in range(1,6):
				n=i*5-j
				ran=[numbr]
				if p[n]==ran:
					check[i-1] +=1
			if check[i-1]==5:
				break
				
		if check[i-1]==5:
				break
				
				
	
		allcount += ncount
mo=allcount/1000	
print mo	
				