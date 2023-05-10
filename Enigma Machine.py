import copy
from curses.ascii import isdigit


class RotorWheel:

    def __init__(self, rotor1_position, rotor2_position, rotor3_position):
        self.rotor1_position = rotor1_position
        self.rotor2_position = rotor2_position
        self.rotor3_position = rotor3_position


Rotors = RotorWheel(1, 1, 1)

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

    translating_to_numbers = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26, }
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
    final_translation = []

    for letter in phrase:
        translation = translation + plug_board_conversions.get(letter)
        translation2 = translating_to_numbers.get(letter)
        # 1st rotor wheel
        if (Rotors.rotor1_position + translation2) > 26:
            translation3 = Rotors.rotor1_position + translation2 - 26
        else:
            translation3 = Rotors.rotor1_position + translation2
        Rotors.rotor1_position += 1
        if Rotors.rotor1_position == 27:
            Rotors.rotor1_position = 1
        if Rotors.rotor1_position == rotor1_starting_point:
            Rotors.rotor2_position += 1

        # 2nd rotor wheel
        if (Rotors.rotor2_position + translation3) > 26:
            translation4 = Rotors.rotor2_position + translation3 - 26
        else:
            translation4 = Rotors.rotor2_position + translation3
        if Rotors.rotor2_position == 27:
            Rotors.rotor2_position = 1
        rotor2_changing_rotor3_position += 1
        if isdigit(rotor2_changing_rotor3_position / 26):
            Rotors.rotor3_position += 1
        if Rotors.rotor3_position == 27:
            Rotors.rotor3_position = 1

        # 3rd rotor wheel
        if (Rotors.rotor3_position + translation3) > 26:
            translation5 = Rotors.rotor3_position + translation4 - 26
        else:
            translation5 = Rotors.rotor3_position + translation4

        # reflector plate
        if Rotors.rotor1_position > 13:
            Rotors.rotor1_position = Rotors.rotor1_position - 13
        else:
            Rotors.rotor1_position = Rotors.rotor1_position + 13

        if Rotors.rotor2_position > 13:
            Rotors.rotor2_position = Rotors.rotor2_position - 13
        else:
            Rotors.rotor2_position = Rotors.rotor2_position + 13

        if Rotors.rotor3_position > 13:
            Rotors.rotor3_position = Rotors.rotor3_position - 13
        else:
            Rotors.rotor3_position = Rotors.rotor3_position + 13

        # 3rd wheel 2nd time
        if (Rotors.rotor3_position + translation5) > 26:
            translation6 = Rotors.rotor3_position + translation5 - 26
        else:
            translation6 = Rotors.rotor3_position + translation5

        # 2nd wheel 2nd time
        if (Rotors.rotor2_position + translation6) > 26:
            translation7 = Rotors.rotor2_position + translation6 - 26
        else:
            translation7 = Rotors.rotor2_position + translation6

        # 1st wheel 2nd time
        if (Rotors.rotor1_position + translation7) > 26:
            translation8 = Rotors.rotor1_position + translation7 - 26
        else:
            translation8 = Rotors.rotor1_position + translation7

        final_translation.append(rotor_possible_positions.get(translation8))

    return "".join(str(e) for e in final_translation)


print(translate(input("Enter a phrase: ")))
