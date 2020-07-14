import random


def test():
    full_list = []
    n = ' '



    gameboard = {
        'a1': n, 'a2': n, 'a3': n,
        'b1': n, 'b2': n, 'b3': n,
        'c1': n, 'c2': n, 'c3': n
    }

    comp_inp_dict = {

        1: 'a1', 2: 'a2', 3: 'a3',
        4: 'b1', 5: 'b2', 6: 'b3',
        7: 'c1', 8: 'c2', 9: 'c3'
    }

    def printBoard(gameboard):
        print(gameboard['a1'] + '|' + gameboard['a2'] + '|' + gameboard['a3'])
        print('-+-+-')
        print(gameboard['b1'] + '|' + gameboard['b2'] + '|' + gameboard['b3'])
        print('-+-+-')
        print(gameboard['c1'] + '|' + gameboard['c2'] + '|' + gameboard['c3'])

    printBoard(gameboard)

    print(gameboard)

    while len(full_list) <= 8:
        user = input('> ')


        gameboard[user] = 'X'
        full_list.append('x')


        comp = random.randint(1,9)
        gameboard[comp_inp_dict[comp]] = 'O'
        full_list.append('o')

        def printBoard(gameboard):
            print(gameboard['a1'] + '|' + gameboard['a2'] + '|' + gameboard['a3'])
            print('-+-+-')
            print(gameboard['b1'] + '|' + gameboard['b2'] + '|' + gameboard['b3'])
            print('-+-+-')
            print(gameboard['c1'] + '|' + gameboard['c2'] + '|' + gameboard['c3'])
        printBoard(gameboard)




    return print(gameboard)

test()
