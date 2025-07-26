with open("newfile.txt","r") as file:
    for line in file:
        print(line.split(" "))
        print(line)