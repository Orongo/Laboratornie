def get_k(x1,y1,x2,y2):
	return (x2-x1)/(y2-y1)
ar = [int(i) for i in input().split(',')]
print("YES" if (len(ar) == 8) and  (get_k(*ar[:4])==get_k(*ar[4:])) else "NO")
