def readf(type):
    if type == 1:
        with open('../лаба4/example.txt.txt', 'r', encoding="utf-8") as file:
            content = file.read()
            print(content)
    elif type == 2:
        with open('../лаба4/example.txt.txt', 'r', encoding="utf-8") as file:
            for line in file:
                print(line)
    else:
        print('no')
readf(1)









