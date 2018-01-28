# Loops in Python!
# For Mobile App Class
#
# my_variable = "hello"
#
# for character in my_variable: # iterable
#     print(character)
#
# my_list = [1, 3, 5, 7, 9]
#
# for number in my_list:
#     print(number ** 2)

# want_number = True
# while want_number == True:
#     print(10)
#     user_input = input('Should we print again? (y/n) ')
#     if user_input == 'n':
#         want_number = False

# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")
#
# if person in known_people:
#     print("You know {}!".format(person))
# else:
#     print("You Don't know {}!".format(person))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
# def even_numbers():
#     evens = []
#     the_evens = [2, 4, 6, 8, 10]
#     for number in numbers:
#         if number in the_evens:
#             evens.append(number)
#     return evens

def even_numbers():
    evens = []
    for number in numbers:
        if number % 2 == 0: # Modules returns division remainder
            evens.append(number)
    return evens

print(even_numbers())


# Modify the below method so that "Quit" is returned if the choice parameter is "q".
# Don't remove the existing code
def user_menu(choice):
    if choice == "a":
         return "Add"
    elif choice == "q":
         return "Quit"


print(user_menu("q"))


