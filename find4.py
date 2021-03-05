wordCheck = raw_input("please enter the word you would like to check the spelling of: ")
with open("1.txt", "r") as f:
    found = False    
    for line in f:
        if line.strip() == wordCheck:
            print ('That is the correct spelling for '+ wordCheck)
            found = True
            break
    if not found:
        print ( wordCheck+ " is not in our list")
