"""
File: craps.py
Project 9.6
This module studies and plays the game of craps.
Refactors code from case study so that the user
can have the Player object roll the dice and view
the result.
"""
from random import randint


class Die:
    """This class represents a six-sided die."""

    def __init__(self):
        """Creates a new die with a value of 1."""
        self.value = 1

    def roll(self):
        """Resets the die's value to a random number
        between 1 and 6."""
        self.value = randint(1, 6)

    def getValue(self):
        """Returns the value of the die's top face."""
        return self.value

    def __str__(self):
        """Returns the string rep of the die."""
        return str(self.getValue())


class Player(object):

    def __init__(self):
        """Has a pair of dice and an empty rolls list."""
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []
        self.roll = ""
        self.rollsCount = 0
        self.winner = False
        self.loser = False
        self.atStartup = True

    def __str__(self):
        """Returns a string representation of the list of rolls."""
        result = ""
        for (v1, v2) in self.rolls:
            result = result + str((v1, v2)) + " " +\
                     str(v1 + v2) + "\n"
        return result

    def getNumberOfRolls(self):
        """Returns the number of the rolls."""
        return self.rollsCount

    def play(self):
        """Plays a game, saves the rolls for that game,
        and returns True for a win and False for a loss."""
        self.rolls = []
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getValue(),
                    self.die2.getValue())
        self.rolls.append((v1, v2))
        initialSum = v1 + v2
        if initialSum in (2, 3, 12):
            return False
        elif initialSum in (7, 11):
            return True
        while (True):
            self.die1.roll()
            self.die2.roll()
            (v1, v2) = (self.die1.getValue(),
                        self.die2.getValue())
            self.rolls.append((v1, v2))
            laterSum = v1 + v2
            if laterSum == 7:
                return False
            elif laterSum == initialSum:
                return True

    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser

    def rollDice(self):
        self.winner = self.loser = False
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getValue(), self.die2.getValue())
        self.atStartup = False
        self.roll = str((v1, v2))
        self.rollsCount += 1
        initialSum = v1 + v2
        if initialSum in (2, 3, 12):
            self.loser = True
        elif initialSum in (7, 11):
            self.winner = True

        return (v1, v2)


def playOneGame():
    """Plays a single game and prints the results."""
    player = Player()
    player.rollDice()
    print(player.roll)
    if player.isWinner():
        print("You win!")
    elif player.isLoser():
        print("You lose!")

def playManyGames(number):
    """Plays a number of games and prints statistics."""
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in range(number):
        player.rollDice()
        if player.isWinner():
            wins += 1
        elif player.isLoser():
            losses += 1

    print("The total number of wins is", wins)
    print("The total number of losses is", losses)
    print("The average number of rolls per win is %0.2f" % \
          (winRolls / wins))
    print("The average number of rolls per loss is %0.2f" % \
          (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins*100 / number)+"%")

def main():
    """Plays a number of games and prints statistics."""
    number = int(input("Enter the number of games: "))
    playManyGames(number)

if __name__ == "__main__":
    main()
