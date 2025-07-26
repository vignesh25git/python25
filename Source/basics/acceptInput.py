import sys

firstName = sys.argv[1]
lastName = sys.argv[2]

if len(sys.argv) != 3 :
    print("Incorrect argument")
    sys.exit(99)

print(f'welcome to Python programming {firstName} , {lastName}')

