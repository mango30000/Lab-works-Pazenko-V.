def readf(type):
    try:
        if type == 1:
            with open('example.txt.tx','r') as file:
                content = file.read()
                print(content)
        elif type == 2:
            with open('example.txt.tx','r') as file:
                for line in file:
                    print(line)
    except FileNotFoundError:
        print('Файл не существует')
readf(2)