# Special moves

# Break, Continue, Pass

#--- Break : terminate afor loop prematurely

pay_dirt = ['dirt', 'dirt', 'dirt', 'dirt', 'gold', 'dirt', 'dirt', 'dirt']

for scoop in pay_dirt:
    print("PANNING FOR GOLD")
    if scoop == 'gold':
        break
    else:
        print('Just more dirt, gotta keep lookin')

print('=' * 50)

#--- Continue : skip the rest of the current code block and move onto the next iteration in the loop

# square only odd numbers
nums = [12, 256, 1146, 478, 21, 3457]

for num in nums:
    if num % 2 == 0:
        continue
    print("original", num)
    num **= 2
    print("Squared", num)

# Pass : placeholder

my_list = [1,2,3]

for item in my_list:
    pass