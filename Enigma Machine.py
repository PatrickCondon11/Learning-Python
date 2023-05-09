import copy
from curses.ascii import isdigit


def translate(phrase):
    plug_board_conversions = {
        "a": "c",
        "b": "s",
        "c": "n",
        "d": "b",
        "e": "l",
        "f": "v",
        "g": "t",
        "h": "m",
        "i": "e",
        "j": "u",
        "k": "w",
        "l": "d",
        "m": "g",
        "n": "a",
        "o": "q",
        "p": "i",
        "q": "y",
        "r": "j",
        "s": "p",
        "t": "h",
        "u": "z",
        "v": "r",
        "w": "x",
        "x": "f",
        "y": "k",
        "z": "o", }

    rotor_possible_positions = {
        1: "a",
        2: "b",
        3: "c",
        4: "d",
        5: "e",
        6: "f",
        7: "g",
        8: "h",
        9: "i",
        10: "j",
        11: "k",
        12: "l",
        13: "m",
        14: "n",
        15: "o",
        16: "p",
        17: "q",
        18: "r",
        19: "s",
        20: "t",
        21: "u",
        22: "v",
        23: "w",
        24: "x",
        25: "y",
        26: "z", }

    translation = ""
    rotor1_translation = ""
    rotor2_translation = ""
    rotor3_translation = ""
    rotor1_translation2 = ""
    rotor2_translation2 = ""
    rotor3_translation2 = ""
    rotor1_changing_rotor2_position = 0
    rotor2_changing_rotor3_position = 0
    rotor1_starting_point = copy.copy(Rotors.rotor1_position)
    rotor2_starting_point = copy.copy(Rotors.rotor2_position)

    for letter in phrase:
        translation = translation + plug_board_conversions.get(letter)

    for letter in translation:
        rotor1_translation = rotor1_translation + rotor_possible_positions.get(Rotors.rotor1_position)
        Rotors.rotor1_position += 1
        if Rotors.rotor1_position == 27:
            Rotors.rotor1_position = 1
        if Rotors.rotor1_position == rotor1_starting_point:
            Rotors.rotor2_position += 1

    for letter in rotor1_translation:
        rotor2_translation = rotor2_translation + rotor_possible_positions.get(Rotors.rotor2_position)
        rotor2_changing_rotor3_position += 1
        if Rotors.rotor2_position == 27:
            Rotors.rotor2_position = 1
        if isdigit(rotor2_changing_rotor3_position % 26):
            Rotors.rotor3_position += 1
        print(rotor2_starting_point)
        print(rotor2_translation)
        print(Rotors.rotor1_position)
        print(Rotors.rotor2_position)
        print(Rotors.rotor3_position)

    for letter in rotor2_translation:
        rotor3_translation = rotor3_translation + rotor_possible_positions.get(Rotors.rotor3_position)
        if Rotors.rotor3_position == 27:
            Rotors.rotor3_position = 1

    if Rotors.rotor1_position > 12:
        Rotors.rotor1_position = Rotors.rotor1_position - 13
    else:
        Rotors.rotor1_position = Rotors.rotor1_position + 13

    if Rotors.rotor2_position > 12:
        Rotors.rotor2_position = Rotors.rotor2_position + 13
    else:
        Rotors.rotor2_position = Rotors.rotor2_position - 13

    if Rotors.rotor3_position > 12:
        Rotors.rotor3_position = Rotors.rotor3_position - 13
    else:
        Rotors.roto3_position = Rotors.rotor3_position - 13

    for letter in rotor3_translation:
        rotor3_translation2 = rotor3_translation2 + rotor_possible_positions.get(Rotors.rotor3_position)
        if Rotors.rotor3_position == 27:
            Rotors.rotor3_position = 1

    return rotor3_translation2


class Rotors:

    def __init__(self, rotor1_position, rotor2_position, rotor3_position):
        self.rotor1_position = rotor1_position
        self.rotor2_position = rotor2_position
        self.rotor3_position = rotor3_position


Rotors = Rotors(1, 1, 1)
print(translate(input("Enter a phrase: ")))

