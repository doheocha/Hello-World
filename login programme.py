
password = 'horse'



def login(password):
    i = 0
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

login(password)