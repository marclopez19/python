
a=10
b=2

def mcm(a, b):
    def mcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a