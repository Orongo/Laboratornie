ar = [3,4,5,6,7]
print("NO" if len(set(ar))<2 else list(set(sorted(ar)))[-2])