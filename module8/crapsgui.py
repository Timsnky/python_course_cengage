"""
File: crapsgui.py
Project 9.7
Pops up a window that allows the user to play the game of craps.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from craps import Player


class CrapsGUI(EasyFrame):

    def __init__(self):
        """Creates the player, and sets up the Images and labels for the two dice to be displayed, the text area for the game state, and the two command buttons."""
        EasyFrame.__init__(self, title="Craps Game")
        self.setSize(220, 320)
        """Instantiate the model and initial values of the dice"""
        # self.player
        self.player = Player()
        self.v1 = self.player.die1.getValue()
        self.v2 = self.player.die2.getValue()
        """Add labels and buttons to the view"""
        # self.dieLabel1
        self.dieLabel1 = self.addLabel("", row=0, column=0, sticky="NSEW")
        # self.dieLabel2
        self.dieLabel2 = self.addLabel("", row=0, column=1, sticky="NSEW")
        # self.stateArea
        self.stateArea = self.addTextArea("", row=1, column=0, columnspan=2, width=5, height=15)
        # self.rollButton
        self.rollButton = self.addButton(row=2, column=0, text="Roll", command=self.nextRoll)
        # self.addButton
        self.newGameButton = self.addButton(row=2, column=1, text="New game", command=self.newGame)
        self.refreshImages()

    def nextRoll(self):
        """Rolls the dice and updates the view with
        the results."""
        (self.v1, self.v2) = self.player.rollDice()
        self.refreshImages()

    def newGame(self):
        """Create a new craps game and updates the view."""
        self.player = Player()
        self.v1 = self.player.die1.getValue()
        self.v2 = self.player.die2.getValue()
        self.refreshImages()

    def refreshImages(self):
        """Updates the images in the window."""
        fileName1 = "DICE/" + str(self.v1) + ".gif"
        fileName2 = "DICE/" + str(self.v2) + ".gif"
        self.image1 = PhotoImage(file=fileName1)
        self.dieLabel1["image"] = self.image1
        self.image2 = PhotoImage(file=fileName2)
        self.dieLabel2["image"] = self.image2


def main():
    CrapsGUI().mainloop()


if __name__ == "__main__":
    main()
