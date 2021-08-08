from numbers import Number
import numbers

class Polynomial:
    def __init__(self, coefs):     #It has to be self for the first.
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() > 0 and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")
        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return ' + '.join(reversed(terms)) or "0"

    def __eq__(self, other):
        return self.coefficients == other.coefficients

    def __add__(self, other):
        if isinstance(other, Polynomial):
            common = min(self.degree, other.degree) + 1
            coefs = tuple(a + b for a, b in 
                        zip(self.coefficients, other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]
            return Polynomial(coefs)
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,) 
                               + self.coefficients[1:])
        else:
            return NotImplemented
    def __radd__(self, other):
        return self + other

###############################################################
# def __sub__(self, other):
#         if isinstance(other, Polynomial):
#             common = min(self.degree(), other.degree()) + 1
#             coefs = tuple(a - b for a, b in zip(self.coefficients,
#                                                 other.coefficients))
#             coefs -= (self.coefficients[common:] + other.coefficients[common:])

#             return Polynomial(coefs)

#         elif isinstance(other, Number):
#             return Polynomial((self.coefficients[0] - other,)
#                               + self.coefficients[1:])

#         else:
#             return NotImplemented

#     def __rsub__(self, other):
#         return other - self

#     def __mul__(self, other):
#         coefs1 = self.coefficients
#         coefs2 = other.coefficients

#         list1 = [0 for i in range(self.degree() + other.degree() + 1)]
#         if isinstance(other, Number):
#             list1 = [other * i for i in self.coefficients]
#             tuple1 = tuple(list1)
#             return Polynomial(tuple1)
    
#         elif isinstance(other, Polynomial):
#             for i in range(self.degree() + other.degree() + 1):
#                 sum = 0
#                 for j in range(self.degree()+1):
#                     sum += coefs1[j] * coefs2[i - j]
#                 list1[i] = sum
#             return Polynomial(tuple(list1))

#         else:
#             return NotImplemented


#     def __rmul__(self, other):
#         return self * other