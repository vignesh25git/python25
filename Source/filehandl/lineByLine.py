with open("newfile.txt","r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        else:
            print(line)

