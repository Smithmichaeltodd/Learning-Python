print('Please enter your name: ')
name = input() #prompts for name
print('Please enter your password: ')
password = input() #prompts for password
loop = 'True'

while True:

    if name == 'Michael' and password == 'smith111':  # double if statement
        print('Hello Michael')
    if name == 'Michael' and password == 'smith111':
        break

    else:  # two options
        print('Access Denied!')

    if name == 'Michael' and password != 'smith111':
        print('Username is correct!')
    if name != 'Michael' and password == 'smith111':
        print('Password is correct!')
    if name != 'Michael' and password != 'smith111':
        print('Password and username are incorrect!')

    print('Please try again. ')
    print('Please enter your name: ')
    name = input()  # prompts for name
    print('Please enter your password: ')
    password = input()  # prompts for password



