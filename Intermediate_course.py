def learning_lists():
    # Lists: ordered mutable, allows for duplicate elements
        mylist = ["banana", "cherry", "apple"]

    # list index
        item = mylist[2]
        item = mylist[-1]

    # printing all values individually
        for i in mylist:
            print(i)

    # Adding elements to the list
        mylist.append("lemon")
        mylist.insert(1, "blueberry")

    # removing single elements of a list
        mylist.pop()
        mylist.remove("cherry")

    # remove all elements of a list
        mylist.clear()

    # Reverse the order of the list
        mylist.reverse()
    # Sort the list
        mylist.sort()

    # Sort a new or copied list
        new_list = sorted(mylist)
        mylist = ["banana", "cherry", "apple"]

    # Multiplying the number of elements in list
        mylist2 = [0] * 5 + [3, 5, 3, 6]

    # Adding two lists together
        new_list = str(mylist) + str(mylist2)

    # separates parts of a list using colon
        a = mylist[1:5]

        mylist3 = [1, 2 ,3 ,4 ,6]
        b = [i*i for i in mylist3]
        print(b)

        print(mylist.index("cherry"))

        print(mylist)


def learning_tuples():
    # Tuple: ordered, immutable, allows for duplicate elements
        mytuple = tuple(["Max", 28, "Boston"])
        print(mytuple)

    # Checks if element is in the list
        if "Max" in mytuple:
            print("yes")
        else:
            print("no")

    # Checks number of elements in tuple/list
        print(len(mytuple))
    # Counts specific elements in tuple/list
        print(mytuple.count("Max"))

    # Converts tuples to list and vice versa
        mylist4 = list(mytuple)
        mytuple = tuple(mylist4)


def learning_dictionaries():
        mydict = {
            "name": "Max",
            "age": 28,
            "city": "New York"
        }

        mydict2 = dict(name="mary",
                       age=27,
                       city="New York")
    # adds elements
        mydict["email"] = "max@ayx.com"
    # removes elements
        del mydict["name"]
        mydict.pop("age")
