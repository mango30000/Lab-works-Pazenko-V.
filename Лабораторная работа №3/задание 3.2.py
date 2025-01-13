b = input('введите что-нибудь:')
with open('../лаба4/user_input.txt', 'w+') as file:
    file.write(b)

d = input('введите ещё что-нибудь:')
with open('../лаба4/example.txt.txt', 'a') as file:
    file.write(d + '\n')
    




