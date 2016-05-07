str_ = input()
substr = [str_[:i] for i in range(1,len(str_)+1) if len(list(set(str_.split(str_[:i]))))==1 ]
print((substr[0],len(str_.split(substr[0]))-1 ) if len(substr)>1 else "ERROR")