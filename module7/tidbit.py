"""
File: tidbitwithgui.py
Project 8.7

GUI for tidbit program.

Inputs: purchase price and annual interest rate.
"""

from breezypythongui import EasyFrame


class TidbitGUI(EasyFrame):

    def __init__(self):
        """Set up the window and widgets."""
        EasyFrame.__init__(self, title="Tidbit Loan Scheduler")
        """Input fields"""
        # self.addLabel()
        # self.priceField()
        self.addLabel(text="Purchase Price", row=0, column=0)
        self.priceField = self.addFloatField(value=0.0, row=0, column=1)

        # self.addLabel()
        # self.rateField()
        self.addLabel(text="Annual Interest Rate", row=1, column=0)
        self.rateField = self.addFloatField(value=0.0, row=1, column=1)

        """Command button"""
        self.button = self.addButton(text="Compute", row=2, column=0, columnspan=2, command=self.computeSchedule)

        """Output text box"""
        # self.outputArea()
        self.outputArea = self.addTextArea("", row=4, column=0, columnspan=2, width=5, height=15)

    def computeSchedule(self):
        """Event handler for the Compute button."""
        price = self.priceField.getNumber()
        rate = self.rateField.getNumber()
        model = TidbitModel()
        self.outputArea["state"] = "normal"
        self.outputArea.setText(model.compute(price, rate))
        self.outputArea["state"] = "disabled"


class TidbitModel(object):

    def compute(self, purchasePrice, rate):
        rate = rate / 100
        monthly_rate = rate / 12

        downPayment = purchasePrice * 0.1
        purchasePrice = purchasePrice - downPayment
        monthlyPayment = .05 * purchasePrice
        month = 1
        balance = purchasePrice
        result = "Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance\n"
        while balance > 0:
            if monthlyPayment > balance:
                monthlyPayment = balance
                interest = 0
            else:
                interest = balance * monthly_rate

            principal = monthlyPayment - interest
            remaining = balance - principal
            result += "%2d%15.2f%15.2f%17.2f%17.2f%17.2f\n" % (month, balance, interest, principal, monthlyPayment, remaining)

            balance = remaining
            month += 1

        return result

def main():
    """Instantiate and pop up the window."""
    TidbitGUI().mainloop()


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")

