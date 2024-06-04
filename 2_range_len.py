# range() creates a sequence of number that we can iterate through

#-- range(stop) the sequence will go from 0 to stop (non-inclusive)

print(list(range(11)))

for num in range(11):
    print(num)

#-- range(start, stop) : creates a sequence from start (inclusive) to stop (non-inclusive)

print("Range from 5 to 10")
list_of_nums = []

for num in range(5, 11):
    # print(num)
    list_of_nums.append(num)

print(list_of_nums)

print(list(range(5, 11)))

new_list = list(range(5, 11))
print(new_list)

#-- range(start, stop, step) : creates a range from start to stop every step-th number (nth number)

print("Range from 10 to 100, every 10th digit")
for num in range(10, 101, 10):
    print(num)

print("Only even numbers, from 0 to 20")
for num in range(0,21,2):
    print(num)

print("Only even numbers, from 20 to 0")
for num in range(20,0,-2):
    print(num)


#-- range in combination with len()
#indecies   0        1        2         3
alist = ['item1', 'item2', 'item3', 'item4']
print("Length of alist: ")
print(len(alist))
length_of_list = len(alist)

for index in range(len(alist)):
    print(index, alist[index])

# print(alist[4]) - index out of range error

print('=' * 50)

food = ['tacos', 'tiramisu', 'pizza', 'sushi', 'burger', 'caesar salad', 'burger', 'key lime pie']

for index in range(len(food)):
    if food[index] == 'burger':
        print('Burger position:', index)

print('=' * 50)

# Looping over indecies can be very useful when dealing with corresponding lists

students = ['John', 'Jim', 'Jane', 'Jill']
grades = [98, 84, 76, 100]
activities = ['Football', 'Woodshop', 'Art', 'Debate Team']

for index in range(len(grades)):
    print(students[index], "has a grade of", grades[index], 'and their activity is', activities[index])

print('=' * 50)
other_list = []
for item in zip(students, grades, activities):
    # print(item)
    if item[1] < 80:
        other_list.append(item[0])
        print(type(item[0]))
        print(item[0], item[1], item[2])
        other_list.append(item[1])
        other_list.append(item[2])
    print(item[0], "has a grade of", item[1], 'and their activity is', item[2])

print(other_list)