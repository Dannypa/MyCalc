from UFraction import UFraction


class Root:
    def __init__(self, number=1, power: int = 1, k=1):
        self.number = number
        self.power = power
        self.k = k

    def __str__(self):
        return f"{self.k} times {self.power}-th root of {self.number}"

    def __repr__(self):
        return f"number: {self.number}, power: {self.power}, k = {self.k}"

    def execute(self):
        return self.k * (self.number ** (1 / self.power))

    def __mul__(self, other):
        if type(other) not in {Root, int, float, UFraction}:
            raise ValueError("Argument must be a Root, int, float or Ufraction")
        if type(other) != Root:
            self.k *= other
        else:
            if other.power != self.power:


