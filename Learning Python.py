# Learning Python
# Developer: Patrick Condon


# functions and return
def cube(num):
    return num*num*num

print(cube(3))


# Dictionary
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
}
print(month_conversions.get("Jan"))


# exponent function
def raise_to_power(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2,3))


# 2D lists (Matrices)
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][2])
# nested for loop
for row in number_grid:
    for col in row:
        print(col)


# Translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))


#try and except
try:
    number = int(input("Enter a number : "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

readme_file = open("README.md", "r")

print(readme_file.readable())

readme_file.close()