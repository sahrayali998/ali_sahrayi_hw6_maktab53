remove_none = [1, None, "hi", 55, -9, None, None, 1.1]
rm = list(filter(lambda word: word != None, remove_none))
print(rm)