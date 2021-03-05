
fd = open("addresses.txt","r")    # open the file in read mode
file_contents = fd.read()   # read file contents
word = "1DepYXHhCfAheuRe6ev8gqnA1hgnGVXgWM"              # input word to be searched
if(word in file_contents):  # check if word is present or not
    print("word found")
else:
    print(word)
    print("word not found")
    
fd.close()                  # close the file
