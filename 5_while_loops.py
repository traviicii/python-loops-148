# While loops allow us to repeat code while a condition is true

# it will continue to run until the condition is False or we break out of the loop

# syntax

#while (condition):
#   run code block

bus = []

# my buss can only hold 5 people

while len(bus) < 5:
    print("Letting a person on the bus")
    print("People on the bus:", len(bus))
    bus.append("Person")

print(bus)

# be careful about infinite loops

flag = True

while flag:
    user = input("Say something, but if you wanna quite, then say so ")
    if user == 'quit':
        # flag = False
        break

# watch out for failure to launch
# the loop's condition starts as False and never runs

bus = []

while len(bus) > 5:
    print("Letting a person on the bus")
    print("People on the bus:", len(bus))
    bus.append("Person")