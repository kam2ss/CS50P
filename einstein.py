"""
A program that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent
number of joules as an integer.
"""

def main():
    mass = int(input("m: "))
    einstein(mass)

def einstein(m):
    c = 300000000
    E = m * (c ** 2)
    print(E)

if __name__ == "__main__":
    main()