"""
A program that prompts the user for input and then outputs that same input, replacing each space
with ... (three periods).
"""

def main():
    playback()

def playback():
    text = input("").replace(" ", "...")
    print(text)

if __name__ == "__main__":
    main()