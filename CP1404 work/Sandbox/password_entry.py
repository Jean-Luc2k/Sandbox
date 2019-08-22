"""Jean-Luc Andreassen"""

MINIMUM_LENGTH = 6


def main():
    password = input("Please enter a password of at least 6 letters: ")
    while len(password) < MINIMUM_LENGTH:
        password = input("That password is invalid, please enter at least 6 letters: ")

    print("*"*len(password))


main()
