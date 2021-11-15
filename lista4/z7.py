def write_list(list):
    print(' '.join([str(item) for item in list]).center(30))

x = int(input("Podaj ilość wyrazów: "))
line = [1]
lista = [1]
print(lista)
for i in range(x-1):
    next_line = [1]
    for j in range(len(line) - 1):
        next_line.append(line[j] + line[j + 1])
    next_line.append(1)
    line = next_line
    lista.append(line)
    print(line)
