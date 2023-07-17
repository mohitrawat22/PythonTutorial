f = open('files/myfile1.txt', 'r')
text = f.read()
print(text)
f.close()

f = open('files/myfile2.txt', 'w')
f.write('Hello World 1')
f.close()

f = open('files/myfile2.txt', 'a')
f.write('Hello World 2')
f.close()

# "with" is used so that you don't need to close the file
# file will get closed automatically
with open('files/myfile2.txt', 'a') as f:
    f.write('Hello World 3')


f = open('files/myfile3.txt', 'r')
while True:
    line = f.readline()
    print(line)
    if not line:
        break

f = open('files/myfile1.txt', 'r')
f.seek(3)
print(f.tell())
data = f.read(5)
print(data)

f = open('files/myfile4.txt', 'w')
lines = ['Hello1\n', 'Hello2\n', 'Hello3\n']
f.writelines(lines)
f.close()

with open('files/myfile5.txt', 'w') as f:
    f.write('Hello World')
    f.truncate(5)
