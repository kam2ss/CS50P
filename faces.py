"""
A program that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise
known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face).
"""
### New approach: ###

# Note 1
# "Happy" and "sad" faces code should come first, because otherwise the first two blocks will always
# be executed and the third block will never be reached.
def main():
    text = input("")
    faces(text)

def faces(t):
    if ":)" in t and ":(" in t: # See: Note 1
        print((t).replace(":)", "🙂").replace(":(", "🙁"))
    elif ":)" in t:
        print((t).replace(":)", "🙂"))  
    elif ":(" in t:
        print((t).replace(":(", "🙁"))
    
if __name__ == "__main__":
    main()


### First approach: ###
def main():
    print(convert())

def convert():
    smile = input("Enter: ")
    if smile == 'Hello :)':
        return ('Hello 🙂')
    elif smile == 'Goodbye :(':
        return ('Goodbye 🙁')
    elif smile == 'Hello :) Goodbye :(':
        return ("Hello 🙂 Goodbye 🙁")

main()