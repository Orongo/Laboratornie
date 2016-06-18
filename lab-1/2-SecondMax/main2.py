ar = [int(i) for i in input().split(',')]
print("NO" if len(set(ar))<2 else list(set(sorted(ar)))[-2])
