file = open("newfile.txt","w")

file.write("Hello first line\n")
file.write("Second line\n")
file.write("To be continued")

file.close()

file = open("newfile.txt","r")
content = file.read()
print(content)

"""
Modes (One-Liner Summary):

Mode   Description
'r'    Read-only (file must exist)
'w'    Write-only (overwrites or creates)
'a'    Append-only (adds to end of file)
'r+'   Read + write (file must exist)
'w+'   Write + read (overwrites or creates)
'a+'   Append + read (creates if not exists)
'rb'   Read binary
'wb'   Write binary
'ab'   Append binary
"""