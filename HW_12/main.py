# 1
f = open('hw.txt', 'w')
f.write('Hi\n')
f.close()

# 2
with open('hw.txt', 'r') as f:
    print(f.read())

# 3
with open('hw.txt', 'a') as f:
    f.write('Maks')

# 4
with open('hw.txt', 'r') as f:
    print(f.read())

# 5
n = open('new.txt', 'w')
while True:
    line = input('Write smth:')
    if line == 'exit':
        break
    n.write(line + '\n')
n.close()