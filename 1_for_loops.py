# Intro to For Loops

# Aloow us to execute a code block for every item in an iterable (strings, lists, ...)

# They allow us to repeate code a limited number of times (number of times is determined by the size of the iterable)

# syntax of For Loops

#for item in iterable:
#   code block

flavors = ['vanilla', 'chocolate', 'mint', 'caramel']

for flavor in flavors:
    # print("Running this code block")
    # print(flavor)
    print("Tasting the", flavor, 'flavor')

# As we loop over an iterable we get to isolate each item and can choose to do something with that item or not

guest_list = ['Dylan', 'Travis', 'Christian', 'Sarah', 'Shoha']

line = ['Adam', 'Craig', 'Dylan', 'Travis', 'Christian', 'Billy Bob']

# door man loop

for person in line:
    print('*', person, 'walks up*')
    if person in guest_list:
        print("Welcome to the party!!")
    else:
        print("Get outta here!!")


submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

for student in submitted:
    if student in attended:
        print(student, "submitted HW and attended class")
    else:
        print(student, "submitted HW but didn't attend class")


nums = [12, 234, 567, 98, 1234567, 145, 178, 15326]

for num in nums:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

print('=' * 50)
for num in nums:
    if num == 98:
        print("this is the the number", num)
    elif num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")