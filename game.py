from tkinter import *
import random

root = Tk()

winner_label = Label(root, text = 'good luck!')
win_list = []

def game(player_inp):
  if len(win_list) < 3:
    player_win = 'Win!'
    comp_win = 'You lose!'
    comp_choice = ['rock', 'paper', 'scissors']
    comp_choice_f = random.choice(comp_choice)
    
    global winner_label
    global counter_label

    if comp_choice_f == player_inp:
        winner_label.grid_forget()
        winner_label = Label(root, text = 'its a tie!')
        winner_label.grid(row = 3, column = 1)
        win_list.append('its a tie')

        counter_label.grid_forget()
        counter_label = Label(root, text = str(len(win_list)) + ' of 3')
        counter_label.grid(row = 2, column = 1, pady = 10)

    elif comp_choice_f == 'rock' and player_inp == 'paper':
        winner_label.grid_forget()
        winner_label = Label(root, text = player_win)
        winner_label.grid(row = 3, column = 1)
        win_list.append(player_win)

        counter_label.grid_forget()
        counter_label = Label(root, text = str(len(win_list)) + ' of 3')
        counter_label.grid(row = 2, column = 1, pady = 5)

    elif comp_choice_f == 'rock' and player_inp == 'scissors':
        winner_label.grid_forget()
        winner_label = Label(root, text = comp_win)
        winner_label.grid(row = 3, column = 1)
        win_list.append(comp_win)

        counter_label.grid_forget()
        counter_label = Label(root, text = str(len(win_list)) + ' of 3')
        counter_label.grid(row = 2, column = 1, pady = 10)

    elif comp_choice_f == 'paper' and player_inp == 'rock':
        winner_label.grid_forget()
        winner_label = Label(root, text = comp_win)
        winner_label.grid(row = 3, column = 1)
        win_list.append(comp_win)

        counter_label.grid_forget()
        counter_label = Label(root, text = str(len(win_list)) + ' of 3')
        counter_label.grid(row = 2, column = 1, pady = 10)

    elif comp_choice_f == 'paper' and player_inp == 'paper':
        winner_label.grid_forget()
        winner_label = Label(root, text = player_win)
        winner_label.grid(row = 3, column = 1)
        win_list.append(player_win)

        counter_label.grid_forget()
        counter_label = Label(root, text = str(len(win_list)) + ' of 3')
        counter_label.grid(row = 2, column = 1, pady = 10)

    elif comp_choice_f == 'scissors' and player_inp == 'paper':
        winner_label.grid_forget()
        winner_label = Label(root, text = comp_win)
        winner_label.grid(row = 3, column = 1)
        win_list.append(comp_win)

        counter_label.grid_forget()
        counter_label = Label(root, text = str(len(win_list)) + ' of 3')
        counter_label.grid(row = 2, column = 1, pady = 10)

    elif comp_choice_f == 'scissors' and player_inp == 'rock':
        winner_label.grid_forget()
        winner_label = Label(root, text = player_win)
        winner_label.grid(row = 3, column = 1)
        win_list.append(player_win)

        counter_label.grid_forget()
        counter_label = Label(root, text = str(len(win_list)) + ' of 3')
        counter_label.grid(row = 2, column = 1, pady = 10)


  elif len(win_list) <= 3:

      player = win_list.count('Win!')
      comp = win_list.count('You lose!')
      if player > comp:
          winner_label.grid_forget()
          winner_label = Label(root, text = 'Congratulations, you win the game!')
          winner_label.grid(row = 3, column = 1)
          score_label = Label(root, text = 'Player = ' + str(player) + '   Computer = ' + str(comp))
          score_label.grid(row = 6, column = 0, columnspan = 2)


          restart_button = Button(root, text = 'Restart game', command =lambda: win_list.clear())
          restart_button.grid(row = 4, column = 1)
          last_round = Label(root, text='The score last round was:')
          last_round.grid(row=5, column=1)
      elif comp > player:
          winner_label.grid_forget()
          winner_label = Label(root, text='Comiserations, you lost the game!')
          winner_label.grid(row=3, column=1)
          score_label = Label(root, text='Player = ' + str(player) + '   Computer = ' + str(comp))
          score_label.grid(row=6, column=0, columnspan=2)


          restart_button = Button(root, text='Restart game', command=lambda: win_list.clear())
          restart_button.grid(row=4, column=1)
          last_round = Label(root, text='The score last round was:')
          last_round.grid(row = 5, column = 1)









Intro_label = Label(root, text = 'Rock, Paper, Scissors')


rock = Button(root, text = 'Rock', command = lambda: game('rock'))
paper = Button(root, text = 'Paper', command = lambda: game('paper'))
scissors = Button(root, text = 'Scissors', command = lambda: game('scissors'))

counter_label = Label(root, text = 'go number: ' + str(0))


Intro_label.grid(row = 0, column = 1)
counter_label.grid(row = 2, column = 1, pady = 10)
winner_label.grid(row = 3, column = 1)

rock.grid(row = 1, column = 0)
paper.grid(row = 1, column = 1)
scissors.grid(row = 1, column =2)

root.mainloop()