var1 = 'Hi'
var2 = 'Hi'

num1 = 2
num2 = 8

def my_print_method(my_parameter):
    print(my_parameter)


def my_multiply_method(number_one, number_two):
    return number_one * number_two


# Complete the method by making sure it returns 42. .
def return_42():
    # Complete method here
    return(42)


# Create a method below, called my_method, that takes two arguments and returns the result of its two arguments multiplied together.
def my_method(number_one, number_two):
    return number_one * number_two


print(num1 * num2)

my_print_method('Hello world!')

result = my_multiply_method(5, 3)
my_print_method(result)

my_print_method(my_multiply_method(5, 3))


print(return_42())

print(my_method(3, 5))


## Exercise

def who_do_you_know():
    # Ask the user for a list of people they know
    people = input("Enter the names of people you know, separated by commas: ")

    # Split the string into a list
    people_list = people.split(",")
    people_without_spaces = []
    for person in people_list:
        people_without_spaces.append(person.strip())

    # Return that list
    return people_without_spaces


def ask_user():
    # Ask user for a name
    person = input("Enter a name of someone you know: ")

    # See if their name is in the list of people they know
    if person in known_people:
        # Print out that they know the person
        print("You know {}!".format(person))
    else:
        print("Who the heck is {}?".format(person))

# Enter people you know
known_people = who_do_you_know()

# Ask for a person to look up
ask_user()
