def print_p(M,N):
	for i in range(1,N+1):
		print("{p:_>{len_p}}=_{i:_>{len_i}}_{M}".format(p=M*i,len_p=len(str(M*N)),i=i,len_i=len(str(N)),M=M))
M,N = (int(i) for i in input().split(','))
print_p(M,N)