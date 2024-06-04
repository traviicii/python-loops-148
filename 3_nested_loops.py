# nested loops

# a loop inside of a loop

nums = [1,2,3,4]
other = ["this", 'that', 'another thing']

# for num1 in nums:
#     print("this is our outter loop iteration:", num1)
#     for num2 in nums:
#         print("This is our Inner loop iteration: ", num2)

for num in nums:
    print('this is our outer loop: ', num)
    for thing in other:
        print("inside our inner loop", thing)

print('='*50)

#-- Topping combinations

pizza_type = ['deep dish', 'cicilian', 'NY style', 'Detroit']
toppings = ['pepperoni', 'sausage', 'ham', 'pineapple', 'olives']

# for topping_1 in toppings:
#     for topping_2 in toppings:
#         if topping_1 == topping_2:
#             print("Double", topping_1)
#         else:
#             print(topping_1, topping_2)

for type1 in pizza_type:
    for topping in toppings:
        print("I have a ", type1, "pizza with", topping)