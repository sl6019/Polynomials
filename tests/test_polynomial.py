from polynomials import Polynomial


def test_print():

    p = Polynomial((2, 1, 0, 3))

    assert str(p) == "3x^3 + x + 2"

def test_equility():
    assert Polynomial((0, 1)) == Polynomial((0, 1))