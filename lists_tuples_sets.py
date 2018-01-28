# Lists, Tuples and Sets

list_grades = [77, 80, 90]
tuple_grades = (77, 80, 90) # immutable

set_grades = {77, 80, 90} # unique & unordered

set_grades.add(60)
set_grades.add(60)
print(set_grades)


## Set operations

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

print(your_lottery_numbers.intersection(winning_numbers))
print(your_lottery_numbers.union(winning_numbers))
print(your_lottery_numbers.difference(winning_numbers))
print(winning_numbers.difference(your_lottery_numbers))

def adding_simplified(arg_list):
    return sum(arg_list)

print(adding_simplified([13, 45, 66, 3, 4]))


# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [20, 30, 50]
print(sum(my_list))

# Create a tuple, called my_tuple, with a single value in it
my_tuple = (1,)
print(my_tuple)

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {1, 5, 77, 9, 12, 99}
print(set1.intersection(set2))
