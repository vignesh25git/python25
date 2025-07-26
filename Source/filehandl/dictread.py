import csv

with open("input.txt","r") as file:
    reader = csv.DictReader(file)
    for row1 in reader:
        print(row1["Age"])

with open("input.txt","r") as file:
    line = file.readline()
    for line in file:
        

