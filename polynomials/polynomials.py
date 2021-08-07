class Polynomial:
    def __init__(self, coefs):     #It has to be self for the first.
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1
