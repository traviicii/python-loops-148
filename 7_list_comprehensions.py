# List comprehensions are inline for loops that produce a list

# syntax
# var = [<added item> for item in iterable]

# List comprehension with a For loop

students = [1, 2, 3]

shirt_list = [num * 2 for num in students]
print(shirt_list)

other_list = []
for num in students:
    other_list.append(num * 2)

print(other_list)

print('=' *50)

# List comprehension with an If statement

# syntax
# var = [<added item> for item in iterable if (condition)]

nums = [1,2,3,4,5,6]

evens = [num + 2 for num in nums if num % 2 == 0]
print(evens)

evens2 = []
for num in nums:
    if num % 2 == 0:
        evens2.append(num + 2)
print(evens2)

divider = '=' *50
print(divider)

# list comp with 'if' and 'else'

# syntax

# var = [<if true add> if (condition) else <else add> for item in iterable]

grades = [100, 98, 52, 87, 98, 68]

pass_fail = ['pass' if grade >= 70 else 'fail' for grade in grades]
print(pass_fail)