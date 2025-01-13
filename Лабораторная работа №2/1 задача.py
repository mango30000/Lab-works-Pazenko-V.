def greet(name):
    print('Привет,', name, '!')

greet('Ксюша')


def square(number):
    return number**2

print(square(3))


def max_of_two(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return 'Два числа одинаковы'
print(max_of_two(2, 6))
