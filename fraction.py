class Fraction:
    def __init__(self, /, w: int = None, *, n: int, d: int) -> None:
        self._whole = w
        self._numerator = n
        self._denominator = d

    def whole(self) -> int:
        if self._whole is None:
            return 0
        return self._whole

    def numerator(self) -> int:
        return self._numerator

    def denominator(self) -> int:
        return self._denominator


frac = Fraction(3, n=2, d=5)
print(frac.numerator())
print(frac.denominator())
print(frac.whole())
