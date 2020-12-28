A = {}
with open('practice_22.txt') as f:
	line = f.readline()
	while line:
               line = line.strip()
               if line in A:
                        A[line] += 1
               else:
                        A[line]=1
               line = f.readline()

print(A)