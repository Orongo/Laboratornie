obj = 1 #Ввели объект
print(" ".join([i for i in dir(obj) if not i.startswith('_')]))  #Магия