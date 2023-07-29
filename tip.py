"""
A program that calculates the tip when entered in percentage.
"""

def main():
    dollors = dollors_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollors * percent/100
    print(f"Leave ${tip:.2f}")

def dollors_to_float(d):
    return float(d.strip("$"))

def percent_to_float(p):
    return float(p.strip("%"))

if __name__ == "__main__":
    main()