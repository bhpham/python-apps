#Read files
# file = open('test.txt', mode = 'r')

# data = file.readlines()
# print(data)

# file.close()


#Creating files 
try:
    with open('sample/newfile.txt' , 'a') as file:
        file.writelines(["\nThis is a new file created!", "\nThis is another to be added"])
except FileNotFoundError as e:
    print("Error", e)