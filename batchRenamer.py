# A batch renamer that basically leverages Windows Explorer's batch renaming scheme to convert to a [name][key].[fileExtension] pattern. 
# I made this as practice and since I face this situation a lot working with series of files, made sense to scriptify it and hone my GitHub skills at the same time
#
# It's also my first public project so I get over myself

import os

def main (): 

    #When you select a bunch of files in Windows Explorer and rename them all at once, it takes in a filename and then adds a space and an index number inside parentheses. 
    patternKey = str(input("Please enter the key of the file name pattern. Example filename with a pattern key: patternKey (1).jpg: "))
    #Taking in the pattern key of the user's choice
    userPatternKey = str(input("Please enter the REPLACEMENT KEY of the file name pattern INCLUDING WHITESPACES. Example filename with a pattern key: patternKey (1).jpg: "))
    fileExtension = input("Please specify the file extension: ") 

### This block is for getting the right input for the range and then catching the error if some smartass decides enter a string
    while True:
        try:
            fileRange1 = int(input("Please enter the first number in the range: "))
            break
        except ValueError:
            print("Please enter a valid number")
    
    while True:
        try:
            fileRange2 = int(input("Please enter the second number in the range: "))
            fileRange2 += 1
            break
        except ValueError:
            print("Please enter a valid number")



# I iterate over a simple range, renaming along the way
    for key in range(1,11): 
            print(key)
            if len(str(key))==2:
                os.rename("{} ({}).{}".format(patternKey, key,fileExtension),"{}{}.{}".format(userPatternKey,key,fileExtension))
            else:
                os.rename("{} ({}).{}".format(patternKey,key,fileExtension),"{}{}.{}".format(userPatternKey,key,fileExtension))



if __name__ == '__main__':
    main()