'''
Linda Morales and Mitchell Coffin
lmorale4@binghamton.edu
mcoffin1@binghamton.edu
'''
# Imports
# import tkinter
from tkinter import messagebox
from tkinter import *
import match
import random

# class that matches molecule names to their structures and
# informs you if you are correct or not
class MatchGUI:

  # Collaborative coding
  # Constructor----------------------------------------------------------
  def __init__(self):
    # Constants-------------------------------------
    self.__MOLECULE_HEIGHT = '100'
    self.__MOLECULE_WIDTH = '100'
    self.__NAME_WIDTH = '12'
    self.__BUTTON_COLOR = 'lightgrey'
    self.__CORRECT_COLOR = 'lightgreen'
    self.__STICK_TO_NSEW = 'nswe'
    
    # Window
    
    self.__win = Tk()
    self.__win.title('ChemMatch')

    # Menu
    self.__menuOp = Menu(self.__win)
    self.__menuOp.add_command(label='Instructions',\
                              command=self.printInstructions)
    self.__menuOp.add_command(label='Restart', command=self.restart)
    self.__menuOp.add_command(label='Quit', command=self.quitGame)
    self.__win.config(menu=self.__menuOp)

    # Models/Vsriables
    self.__clickedButtons = []
    self.__buttonText = []
    self.__allButtons = []
    self.__model = match.Match(match.CHEMDICT)
    self.__dictKeysList = self.__model.getDictKeys()
    self.__dictKeysList.sort()
    self.__dictValuesList = self.__model.getDictValues()
    self.__dictValuesList.sort()
    self.__scoreCount = IntVar()
    self.__scoreCount.set(0)

    # Score Frame
    self.__scoreFrame = Frame(self.__win)

    # Score Labels
    self.__scoreLabel = Label(self.__scoreFrame, textvariable=self.__scoreCount)
    self.__scoreNameLabel = Label(self.__scoreFrame, text='Score:')
    
    # Buttons Frame
    self.__buttonFrame = Frame(self.__win)

    # Import photos
    photo1 = PhotoImage(file = 'ethyne.png')
    photo2 = PhotoImage(file = 'ethane.png')
    photo3 = PhotoImage(file = 'propane.png')
    photo4 = PhotoImage(file = 'benzene.png')
    photo5 = PhotoImage(file = 'pxylene.png')
    photo6 = PhotoImage(file = 'methane.png')
    photo7 = PhotoImage(file = 'water.png')



    # Molecule Buttons    
    self.__molecule1 = Button(self.__buttonFrame, text=self.__dictKeysList[0],\
                              image = photo1, height=self.__MOLECULE_HEIGHT,\
                              width=self.__MOLECULE_WIDTH,\
                              command=lambda:self.appendButtonToList\
                              (self.__molecule1), bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__molecule1)

    self.__molecule2 = Button(self.__buttonFrame, text=self.__dictKeysList[1],\
                              image = photo2, height=self.__MOLECULE_HEIGHT, \
                              command=lambda:self.appendButtonToList\
                              (self.__molecule2), bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__molecule2)

    self.__molecule3 = Button(self.__buttonFrame, text=self.__dictKeysList[2],\
                              image = photo3,height=self.__MOLECULE_HEIGHT,\
                              command=lambda:self.appendButtonToList\
                              (self.__molecule3),bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__molecule3)
    
    self.__molecule4 = Button(self.__buttonFrame, text=self.__dictKeysList[3],\
                              image = photo4,height=self.__MOLECULE_HEIGHT,\
                              command=lambda:self.appendButtonToList\
                              (self.__molecule4), bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__molecule4)
    
    self.__molecule5 = Button(self.__buttonFrame, text=self.__dictKeysList[4],\
                              image = photo5, height=self.__MOLECULE_HEIGHT,\
                              command=lambda:self.appendButtonToList\
                              (self.__molecule5), bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__molecule5)
    
    self.__molecule6 = Button(self.__buttonFrame, text=self.__dictKeysList[5],\
                              image = photo6,height=self.__MOLECULE_HEIGHT,\
                              command=lambda:self.appendButtonToList\
                              (self.__molecule6), bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__molecule6)
    
    self.__molecule7 = Button(self.__buttonFrame, text=self.__dictKeysList[6],\
                              image = photo7,height=self.__MOLECULE_HEIGHT,\
                              command=lambda:self.appendButtonToList\
                              (self.__molecule7), bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__molecule7)
    
    
    # Name Buttons
    self.__name1 = Button(self.__buttonFrame, text=self.__dictValuesList[0],\
                          command=lambda:self.appendButtonToList(self.__name1),\
                          width=self.__NAME_WIDTH, bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__name1)
    
    self.__name2 = Button(self.__buttonFrame, text=self.__dictValuesList[1],\
                          command=lambda:self.appendButtonToList(self.__name2),\
                          bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__name2)
    
    self.__name3 = Button(self.__buttonFrame, text=self.__dictValuesList[2],\
                          command=lambda:self.appendButtonToList(self.__name3),\
                          bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__name3)
    
    self.__name4 = Button(self.__buttonFrame, text=self.__dictValuesList[3],\
                          command=lambda:self.appendButtonToList(self.__name4),\
                          bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__name4)
    
    self.__name5 = Button(self.__buttonFrame, text=self.__dictValuesList[4],\
                          command=lambda:self.appendButtonToList(self.__name5),\
                          bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__name5)
    
    self.__name6 = Button(self.__buttonFrame, text=self.__dictValuesList[5],\
                          command=lambda:self.appendButtonToList(self.__name6),\
                          bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__name6)
    
    self.__name7 = Button(self.__buttonFrame, text=self.__dictValuesList[6],\
                          command=lambda:self.appendButtonToList(self.__name7),\
                          bg=self.__BUTTON_COLOR)
    self.__allButtons.append(self.__name7)
    

    randomNums = self.generateRandomList(0, len(self.__dictKeysList))
    
    # Grid Molecule Buttons
    self.__molecule1.grid(row=randomNums[0], sticky=self.__STICK_TO_NSEW)
    self.__molecule2.grid(row=randomNums[1], sticky=self.__STICK_TO_NSEW)
    self.__molecule3.grid(row=randomNums[2], sticky=self.__STICK_TO_NSEW)
    self.__molecule4.grid(row=randomNums[3], sticky=self.__STICK_TO_NSEW)
    self.__molecule5.grid(row=randomNums[4], sticky=self.__STICK_TO_NSEW)
    self.__molecule6.grid(row=randomNums[5], sticky=self.__STICK_TO_NSEW)
    self.__molecule7.grid(row=randomNums[6], sticky=self.__STICK_TO_NSEW)

    randomNums = self.generateRandomList(0, len(self.__dictKeysList))
    
    #Grid Name Buttons
    self.__name1.grid(row=randomNums[0], column=1, sticky=self.__STICK_TO_NSEW)
    self.__name2.grid(row=randomNums[1], column=1, sticky=self.__STICK_TO_NSEW)
    self.__name3.grid(row=randomNums[2], column=1, sticky=self.__STICK_TO_NSEW)
    self.__name4.grid(row=randomNums[3], column=1, sticky=self.__STICK_TO_NSEW)
    self.__name5.grid(row=randomNums[4], column=1, sticky=self.__STICK_TO_NSEW)
    self.__name6.grid(row=randomNums[5], column=1, sticky=self.__STICK_TO_NSEW)
    self.__name7.grid(row=randomNums[6], column=1, sticky=self.__STICK_TO_NSEW)

    # Grid Labels
    self.__scoreLabel.grid(row=8, column=2, sticky=self.__STICK_TO_NSEW)
    self.__scoreNameLabel.grid(row=8, column=0, sticky=self.__STICK_TO_NSEW)
    
    # Grid button Frame
    self.__buttonFrame.grid()

    # Grid Frame
    self.__scoreFrame.grid()

    # Call mainloop
    mainloop()

  # Predicates -----------------------------------------------------

  # Code by Mitchell
  # Makes sure that the user has clicked 2 buttons before proceeding
  def checkButtonLength(self):
    if len(self.__clickedButtons) >= 2:
      self.checkButtonRow()

  # Mutators --------------------------------------------------------

  # Code by Mitchell
  # Adds the button that was clicked to a list
  # param button (Button) - button that was clicked
  # adds clicked buttons to a list
  def appendButtonToList(self, button):
    self.__clickedButtons.append(button)
    self.checkButtonLength()

  # Code by Mitchell
  # Adds the text from the buttons to a list
  def appendButtonText(self):
    for buttons in self.__clickedButtons:
      self.__buttonText.append(buttons.cget('text'))
    self.setButtons()

  # Code by Linda
  # Checks if the clicked buttons are in the same row,
  # if they are, it deletes the first one chosen
  def checkButtonRow(self):
    if self.__clickedButtons[0].cget('text') in self.__dictKeysList and \
       self.__clickedButtons[1].cget('text') in self.__dictKeysList:
      del self.__clickedButtons[0]
      self.checkButtonLength()
    elif self.__clickedButtons[0].cget('text') in self.__dictValuesList and \
       self.__clickedButtons[1].cget('text') in self.__dictValuesList:
      del self.__clickedButtons[0]
      self.checkButtonLength
    else:
      self.appendButtonText()
      
  # Code by Linda
  # Set keys and values to the right variables in order
  # to check if they match
  def setButtons(self):
    for string in self.__buttonText:
      if string in self.__dictKeysList:
        molecule = string
      else:
        name = string
    self.__model.setMolecule(molecule)
    self.__model.setName(name)
    self.matchButtons()

  # Code by Mitchell
  # Resets lists used to check if buttons matched
  def resetLists(self):
    del self.__clickedButtons[:]
    del self.__buttonText[:]

  # Code by Linda
  # checks if user clicked a name/structure and then
  # clicked the correct corresponding structure/name
  # disables name/structure buttons when correctly done
  def matchButtons(self):
    if self.__model.matchEntries():
      self.correctAnswer()
    else:
      self.incorrectAnswer()
    self.resetLists()

  # Event Handlers------------------------------------------------

  # Menu Buttons

  # Code by Linda
  # Displays messagebox letting user know the instructions
  def printInstructions(self):
    messagebox.showinfo('Instructions','     Match the structure of the \
molecule with its name! Good Luck     ')

  # Collaborative coding
  # Restarts the game by enebling all the buttons and reseting the color,
  # setting the score back to 0,
  # and clearing the lists
  def restart(self):
    for button in self.__allButtons:
      button.config(state=ACTIVE, bg=self.__BUTTON_COLOR)
    del self.__clickedButtons[:]
    del self.__buttonText[:]
    self.__scoreCount.set(0)

  # Collaborative coding
  # Allows user to exit game
  def quitGame(self):
    exit()

  # Code by Mitchell
  # Displays a messagebox saying that asnwer is correct,
  # disables buttons that are correct and changes their color,
  # and adds a point to the score
  def correctAnswer(self):
    messagebox.showinfo('Were you right?', '     Correct!     ')
    self.__scoreCount.set(self.__scoreCount.get() + 1)
    self.__clickedButtons[-1].config(state=DISABLED, bg=self.__CORRECT_COLOR)
    self.__clickedButtons[-2].config(state=DISABLED, bg=self.__CORRECT_COLOR)
    self.allMatchesHaveBeenMade()

  # Code by Mitchell
  # Displays a messagebox saying that answer is incorrect,
  # decreases score by a point
  def incorrectAnswer(self):
    messagebox.showerror('Were you right?', '     Incorrect!     ')
    self.__scoreCount.set(self.__scoreCount.get() - 1)

  # End of game 

  # Code by Linda
  # Checks if all buttons have been matched,
  # displays the user's score,
  # and restarts game
  def allMatchesHaveBeenMade(self):
    buttonCount = 0
    for button in self.__allButtons:
      if button.cget('state') == DISABLED:
        buttonCount += 1
    if buttonCount == len(self.__allButtons):
      messagebox.showinfo('Congrats!', 'You Won!\nYour Score was: %d\nThe \
game will RESTART now.' %self.__scoreCount.get())
      self.restart()
    else:
      buttonCount = 0
    
  # Helper Function----------------------------------------------------

  # Collaborative Coding
  # Generates a random list of nonrepeated numbers given a high and low
  # param minNum (int) - lower bound
  # param maxNum (int) - upper bound
  # return a list of random, non repeating numbers
  def generateRandomList(self, minNum, maxNum):
    numsUsed = []
    for num in range(minNum, maxNum):
      randNum = random.randrange(minNum, maxNum)
      while randNum in numsUsed:
        randNum = random.randrange(minNum, maxNum)
      numsUsed.append(randNum)
    return numsUsed
    
MatchGUI()
