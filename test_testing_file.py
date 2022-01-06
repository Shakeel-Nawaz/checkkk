class Calculate:
    def __init__(self,num1,num2):
        self.n1 = num1
        self.n2 = num2

    def addition(self):
        summed = self.n1 + self.n2
        return summed

    def subtraction(self):
        subbed = self.n2 - self.n1
        return subbed

# class test_calculation:

def test_abc():
    data = Calculate(5,10)
    valu = data.addition()
    assert valu == 15

def test_abc2():
    data = Calculate(5,10)
    valu2 = data.subtraction()
    assert valu2 == 5