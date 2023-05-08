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
    "z": "o",
}

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
    26: "z",
}


def translate(phrase):
    translation = ""

    for letter in phrase:
        translation = translation + plug_board_conversions.get(letter)

    rotor_position = 1
    rotor1_translation = ""
    for letter in translation:
        rotor1_translation = rotor1_translation + rotor_possible_positions.get(rotor_position)
        rotor_position += 1

    return rotor1_translation


print(translate((input("Enter a phrase: "))))


class Rotor:
    def __init__(self, position):
        self.position = position
