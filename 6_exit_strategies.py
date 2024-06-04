# There are 3 ways to exit a while loop

# Break condition, False Falgs, Control variable state

#---- Break, terminate the loop immediately

while True:
    fav_food = input("what's your favorite food? ")

    if fav_food == 'tacos':
        print('That is the correct answer. Enjoy the fiesta!')
        break
    else:
        print("WRONG ANSWER TRY AGAIN")


#--- Flags : allow the rest of the code block to execute but terminate after

searching = True
hours = 0

while searching:
    found = input("Has anyone found my keys? yes or no ")
    if found == 'yes':
        searching = False
    hours += 1
    if not searching:
        print("Thank you for all of your help in finding my keys!")
        print("It only took", hours, "hours")

#---- Control variable - change this condition to eventually be false

count = 0

while count <= 10:
    print('running my code!!!')
    count += 5

