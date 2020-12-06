"""
File: bouncywithgui.py
Project 8.2

Determines the distance traveled by a bouncing ball.

Inputs: Initial height, bounciness index, and number of bounces
"""

from breezypythongui import EasyFrame

def computeDistance(height, index, bounces):
    """Computes the total distance traveled by the ball,
    given an initial height, bounciness index, and
    number of bounces."""
    distance = 0
    for bounce in range(bounces):
        distance += height
        height *= index
        distance += height

    return distance

class BouncyGUI(EasyFrame):

    def __init__(self):
        """Set up the window and widgets."""
        EasyFrame.__init__(self,  title = "Bouncy")

        """Define the following fields"""
        # self.heightField (number entry)
        self.addLabel(text="Initial height", row=0, column=0)
        self.heightField = self.addFloatField(value=0.0, row=0, column=1)

        # self.indexField (number entry)
        self.addLabel(text="Bounciness index", row=1, column=0)
        self.indexField = self.addFloatField(value=0.0, row=1, column=1)

        # self.bouncesField (number entry)
        self.addLabel(text="Number of bounces", row=2, column=0)
        self.bouncesField = self.addIntegerField(value=0, row=2, column=1)

        self.addButton(text="Compute", row=3, column=1, command=self.computeDistance)

        # self.distanceField (result result)
        self.addLabel(text="Total distance", row=4, column=0)
        self.distanceField = self.addFloatField(value=0.0, row=4, column=1, state="readonly")

    def computeDistance(self):
        """
        Event handler for the Compute button and set the
        distanceField.
        """
        height = self.heightField.getNumber()
        index = self.indexField.getNumber()
        bounces = self.bouncesField.getNumber()

        self.distanceField.setNumber(computeDistance(height, index, bounces))

def main():
    """Instantiate and pop up the window."""
    BouncyGUI().mainloop()

if __name__ == "__main__":
    main()

