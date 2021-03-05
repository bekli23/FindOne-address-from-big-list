dicfile = open('addresses.txt', 'r') 
file1 = dicfile.read()
file1 = file1.split()

word = input('enter a word: ') 
if word in file1:
    print('word found',word)
else:
    print('word not found',word)
