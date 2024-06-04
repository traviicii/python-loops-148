# Lecture Notes: Loops

## Intro to For Loops:
- **What is a for loop?** **What does it do?**
    - A for loop, allows us to execute a code block for every item inside an iterable (list, tuple, string, etc.)
- Syntax: 
```python

for item in list:
	Code block
```
- As we loop over an iterable we get to isolate each item and can choose to do something with that item or not

```python
flavors = ["vanilla", "chocolate", "blueberry", "mango", "salted caramel"]

for flavor in flavors:
    print("Mmm... I just sampled " + flavor + "!")
```


## `Range()` and `Range(len())`:
- Generates a sequence of numbers where I can determine the `start, stop, and step`
- `range(stop)`
- `range(start,stop)`
- `range(start, stop step)`
- `range(len(list))` allows us to loop over the indices of a list, using the length of the list

## Nested Loops:
- We can have for loops running inside other for loops

```python
flavors = ['chocolate', 'vanilla', 'strawberry', 'pistachio']
toppings = ['sprinkles', 'chocolate syrup', 'whipped cream', 'cherry']

for flavor in flavors:
    for topping in toppings:
        print("Let's try a scoop of " + flavor + " with some " + topping + " on top!")
```


### Special Moves:
- `break`: Terminates a for loop
- `continue`: Allows you to skip the rest of the code block, and jump to the next iteration
- `pass`: placeholder




## Intro to While Loops:
- A while loop allows us to execute a block of code WHILE a condition is true/ until a condition is no longer true
- Syntax: 
```python
while (condition):
	Codeblock
```

- Be careful of infinite while loops and Non-starting loops

### Exit strategies:
- `break`
- Flag
    - State Change of control variable


## Random Package:
- `.randint(start,stop)` gets you a random num between start and stop inclusive
- `.shuffle()` mixes the order of items in a list
- `.choice`

## List Comprehension:
**Syntax**: 
- `[ <added> for item in iterable]`

```python
numbers = [1, 2, 3, 4, 5]
doubled = [number * 2 for number in numbers]
print(doubled)  # Output: [2, 4, 6, 8, 10]
```

- With `if`/`else`: `[<added> if condition else <added> for item in iterable]`

```python
numbers = [1, 2, 3, 4, 5]
processed = [number * 2 if number > 3 else number for number in numbers]
print(processed)  # Output: [1, 2, 3, 8, 10]
```

- With only `if`: `[<added> for item in iterable if condition]`

```python
numbers = [1, 2, 3, 4, 5]
greater_than_two = [number for number in numbers if number > 2]
print(greater_than_two)  # Output: [3, 4, 5]
```
