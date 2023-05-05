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


class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 3.5, True)
print(student1.gpa)
print(student2.on_honor_roll())


class Chef:
    def make_chicken(self):
        print("The chef made chicken")

    def make_salad(self):
        print("the chef makes a salad")

    def make_special_dish(self):
        print("The chef made bbq ribs")


my_chef = Chef()
my_chef.make_special_dish()


class Chinese_Chef(Chef):

    def make_special_dish(self):
        print("The chef made orange chicken")

    def make_fried_rice(self):
        print("The chef made fried rice")


my_chinese_chef = Chinese_Chef()
my_chinese_chef.make_special_dish()