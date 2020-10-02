# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 02-10-2020
# purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: " + message)

        #
        # Enter your own print statements below:
        print("\n Hope you have a nice day\n")

        # print only first and last of the sentence:
        print("\nfirst:" + message[0])
        print("\nlast:" + message[-1])

        # use slice notation:
        print(""+ message[2:])
        # escaping a character:
        print("\n He said" ' “that’s fantastic”'"!")

        # find all a's in the input word and count how many there are:
        print("message".count('a'))
        print("message".replace('a','-'))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():

    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: " + message)

        # hand the input string to a list and print it out:
        my_list=(message.split(" "))
        print(my_list)
        my_list.append("meee")
        # append a new element to the list and print:

        # remove from the list in 3 ways:
        #my_list.del my_list[3]
        #my_list.remove('meee')
        member = my_list.pop(2)
        print(member)
        # check if the word cake is in your input list:
        #my_list.index("cake")
        # reverse the items in the list and print:
        my_list.reverse()
        print(my_list)
        # reverse the list with the slicing trick:
        print(my_list[::-1])
        # print the list 3 times by using multiplication:
        print(my_list*3)


tas = Types_and_Strings()
tas.play_with_strings()
tas.play_with_lists()