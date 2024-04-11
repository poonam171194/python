file = open('filehandle.txt','r')
print(file.read())

# use readlines

with open('filehandle.txt','r') as file:
    data = file.readline()
    for line in data:
        word = line.split()
        print(word)