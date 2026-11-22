n = int(input("How many characters should be previewed?"))
file = open("To do.txt", "r")
print(file.read())
file.close()
print()

file = open("To do.txt","r")
lines = file.readlines()
file.close()
file = open("To do.txt", "r")
lines = file.readlines()
file.close()

print("Total lines:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()

word = input("Keep lines lines starting with: ")
file = open("To do.txt", "r")
for line in file:
    if line.startswith(word):

        print("keep ->", line.strip())
file.close()
print()
print("The important to do list is given")

file = open("To do.txt", "r")
lines = file.readlines()
file.close()

