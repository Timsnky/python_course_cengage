"""
File: temperatureconverter.py
Project 8.3
Temperature conversion between Fahrenheit and Celsius.
Illustrates the use of numeric data fields.
"""

from breezypythongui import EasyFrame


class TemperatureConverter(EasyFrame):
    """A termperature conversion program."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title="Temperature Converter")

        # self.addLabel (Label for Celsius)
        # self.addLabel (Label for Fahrenheit)
        self.addLabel("Celsius", row=0, column=0)
        self.addLabel("Fahrenheit", row=0, column=1)

        # self.celsiusField (Celsius field)
        # self.fahrField (Fahrenheit field)
        self.celsiusField = self.addFloatField(value=0.0, row=1, column=0)
        self.celsiusField.bind("<Return>", lambda event: self.computeFahr)

        self.fahrField = self.addFloatField(value=32.0, row=1, column=1)
        self.fahrField.bind("<Return>", lambda event: self.computeCelsius)

        # self.addButton (Celsius button)
        # self.addButton (Fahrenheit button)
        self.addButton(text=">>>>", row=2, column=0, command=self.computeFahr)
        self.addButton(text="<<<<", row=2, column=1, command=self.computeCelsius)

    # The controller methods
    def computeFahr(self):
        """Inputs the Celsius degrees
        and outputs the Fahrenheit degrees."""
        fahrenheit = (self.celsiusField.getNumber() * 9 / 5) + 32
        self.fahrField.setNumber(fahrenheit)

    def computeCelsius(self):
        """Inputs the Fahrenheit degrees
        and outputs the Celsius degrees."""
        celsius = (self.fahrField.getNumber() - 32) * 5 / 9
        self.celsiusField.setNumber(celsius)


def main():
    """Instantiate and pop up the window."""
    TemperatureConverter().mainloop()


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")
