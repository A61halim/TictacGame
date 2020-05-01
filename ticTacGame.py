from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sys
from random import randint

ActivP = 1
Player1=[] #what player 1 choose
Player2=[] #what player 2 choose



def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)



root = Tk()
root.title('Tic Tac : Player 1')
 #Make GUI game with tkinter
style = ttk.Style()
style.theme_use('classic')
style.configure('Info.TButton',background='black',font=('Arial',30,'bold'))


playAgain = ttk.Button(root, text='Restart')
playAgain.grid(row=0, column=0,columnspan=3, sticky='snew', ipadx=40, ipady=10)
playAgain.config(command=lambda : restart_program())


button1 = ttk.Button(root, text='')
button1.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
button1.config(command=lambda : ButtonClick(1))
button1.configure(style='Info.TButton')

button2 = ttk.Button(root, text='')
button2.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
button2.config(command=lambda : ButtonClick(2))
button2.configure(style='Info.TButton')

button3 = ttk.Button(root, text='')
button3.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
button3.config(command=lambda : ButtonClick(3))
button3.configure(style='Info.TButton')

button4 = ttk.Button(root, text='')
button4.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
button4.config(command=lambda : ButtonClick(4))
button4.configure(style='Info.TButton')

button5 = ttk.Button(root, text='')
button5.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
button5.config(command=lambda : ButtonClick(5))
button5.configure(style='Info.TButton')

button6 = ttk.Button(root, text='')
button6.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
button6.config(command=lambda : ButtonClick(6))
button6.configure(style='Info.TButton')

button7 = ttk.Button(root, text='')
button7.grid(row=3, column=0, sticky='snew', ipadx=40, ipady=40)
button7.config(command=lambda : ButtonClick(7))
button7.configure(style='Info.TButton')

button8 = ttk.Button(root, text='')
button8.grid(row=3, column=1, sticky='snew', ipadx=40, ipady=40)
button8.config(command=lambda : ButtonClick(8))
button8.configure(style='Info.TButton')

button9 = ttk.Button(root, text='')
button9.grid(row=3, column=2, sticky='snew', ipadx=40, ipady=40)
button9.config(command=lambda : ButtonClick(9))
button9.configure(style='Info.TButton')

#function for event when clicking some button
def ButtonClick(id):
    global ActivP
    global Player1
    global Player2
    if(ActivP == 1):
        setXO(id,'X')
        Player1.append(id)
        root.title('Tic Tac : Player 2')
        ActivP = 2
        AiPlay()
    elif(ActivP == 2):
        setXO(id,'O')
        Player2.append(id)
        root.title('Tic  Tac : Player1')
        ActivP = 1
    winnerChecker()


def setXO(id, text):
    if (id == 1):
        button1.config(text=text)
        button1.state(['disabled'])
    elif (id == 2):
        button2.config(text=text)
        button2.state(['disabled'])
    elif (id == 3):
        button3.config(text=text)
        button3.state(['disabled'])
    elif (id == 4):
        button4.config(text=text)
        button4.state(['disabled'])
    elif (id == 5):
        button5.config(text=text)
        button5.state(['disabled'])
    elif (id == 6):
        button6.config(text=text)
        button6.state(['disabled'])
    elif (id == 7):
        button7.config(text=text)
        button7.state(['disabled'])
    elif (id == 8):
        button8.config(text=text)
        button8.state(['disabled'])
    elif (id == 9):
        button9.config(text=text)
        button9.state(['disabled'])

def winnerChecker():
    winner = -1
    if ((1 in Player1) and (2 in Player1) and (3 in Player1)):
        winner = 1
    if ((1 in Player2) and (2 in Player2) and (3 in Player2)):
        winner = 2

    if ((4 in Player1) and (5 in Player1) and (6 in Player1)):
        winner = 1
    if ((4 in Player2) and (5 in Player2) and (6 in Player2)):
        winner = 2

    if ((7 in Player1) and (8 in Player1) and (9 in Player1)):
        winner = 1
    if ((7 in Player2) and (8 in Player2) and (9 in Player2)):
        winner = 2

    if ((1 in Player1) and (4 in Player1) and (7 in Player1)):
        winner = 1
    if ((1 in Player2) and (4 in Player2) and (7 in Player2)):
        winner = 2

    if ((2 in Player1) and (5 in Player1) and (8 in Player1)):
        winner = 1
    if ((2 in Player2) and (5 in Player2) and (8 in Player2)):
        winner = 2

    if ((3 in Player1) and (6 in Player1) and (9 in Player1)):
        winner = 1
    if ((3 in Player2) and (6 in Player2) and (9 in Player2)):
        winner = 2

    if ((1 in Player1) and (5 in Player1) and (9 in Player1)):
        winner = 1
    if ((1 in Player2) and (5 in Player2) and (9 in Player2)):
        winner = 2

    if ((3 in Player1) and (5 in Player1) and (7 in Player1)):
        winner = 1
    if ((3 in Player2) and (5 in Player2) and (7 in Player2)):
        winner = 2

    if winner == 1:
        messagebox.showinfo(title='cong.', message='the winner is Player 1')
        restart_program()
    if winner == 2:
        messagebox.showinfo(title='cong.', message='the winner is Player 2')
        restart_program()


#AlphaBetta(minimax) algo funtion, to take perfect move
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] # Create a list of empthy place
    move = 0

    #Check for possible winning move to take or to block opponents winning move
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move


    #Try to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    #Try to take the center
    if 5 in possibleMoves:
        move = 5
        return move

    #Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def AiPlay():
    global Player1
    global Player2
    CellVide=[]
    for cell in range(9):
        if(not((cell+1 in Player1) or(cell+1 in Player2))):
            CellVide.append(cell+1)
    if len(CellVide) == 0:
        messagebox.showinfo(title='cong.', message='Game over')
    else:
        IndexRandom=randint(0, len(CellVide)-1)
        ButtonClick(CellVide[IndexRandom])


root.mainloop()
