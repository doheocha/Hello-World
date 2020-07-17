



def login():
    i = 0
    username = ' '
    password = ' '
    x = 0

    if password.isspace() == True and username.isspace() == True:
      while x < 1:
        print('no account detected create new one')
        print('username')
        username = input('>')
        print('password')
        password = input('>')
        x += 10

        if len(password) <= 4:
            print('too short')
            x -= 10

    while i <= 2:
      password_inp = input('> Enter password or type "reset" to change password: ')
      if password_inp == password:
        return print('Computer unlocked')
      elif password_inp == 'reset':
          reset_pwd = input('> Type old password: ')
          if reset_pwd == password:
            password = input('New password: ')
          elif reset_pwd != password:
              return print('Intruder Alert!!!')
      elif password_inp != password:
        i += 1
        if i == 3:
            print('No more attempts; locked out. ')
        elif i < 3:
            print('Wrong password')


login()












