with open("newfile.txt","r") as infile,open("outfile.txt","w") as outfile:
    for line in infile:
        outfile.write(line.strip() + "\n")

