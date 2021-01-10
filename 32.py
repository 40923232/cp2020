def ex_23(1357.txt, 2468.txt):
	C = []
    A = []
    B = []
    
	with open('1357.txt','r') as A:
		line_1 = A.readline()
		while line_1:
			A.append(int(line_1))
			line_1 = 1357.txt.readline()

	with open('2468.txt','r') as B:
		line_2 = B.readline()
		while line_2:
			B.append(int(line_2))
			line_2 = 2468.txt.readline()    
     
        for 1 in range(len(A)):
              if A[1] in B:
                  C.append(A[1])
                  
    return C
    
print (ex_23("1357-1.txt","2468-2.txt"))

