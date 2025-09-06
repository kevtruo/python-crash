chapter_exercise = ['4-1', '4-2', '4-3', '4-4', '4-5', '4-7', '4-8', '4-9','4-10','4-11','4-13']
print(f"Hello user. What chapter exercise are you on? Here are the available chapters: {chapter_exercise}")
chapter_request = input()

if chapter_request in chapter_exercise:
    print(f"\nGreat! You're working on chapter exercise {chapter_request}.")
else:
    print(f"Chapter {chapter_request} is not in the list.")
    chapter_exercise.append(chapter_request)

if chapter_request == '4-1':
    
    # Enter exercise variables below.
    pizzas = ['pepperoni', 'sausage', 'meatlovers']

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    for pizza in pizzas:
        print(f"I like {pizza} pizza.")
    
    print("I really like pizza!")

if chapter_request == '4-2':
    
    # Enter exercise variables below.
    animals = ['dog', 'cat', 'rabbit']

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    for animal in animals:
        print(f"A {animal.title()} would make a great pet.")
    print("All of these animals make great pets!")

if chapter_request == '4-3':

    # Enter exercise variables below.

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    for value in range(1, 21):
        print(value)

if chapter_request == '4-4':

    # Enter exercise variables below.

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    for value in range(1, 1000001):
        if value < 10:
            print(value)

if chapter_request == '4-5':

    # Enter exercise variables below.
    value = list(range(1, 1000001))

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    print(f"Minimum value: {min(value)}")
    print(f"Maximum value: {max(value)}")
    print(sum(value))

if chapter_request == '4-6':

    # Enter exercise variables below.
    odd_value = list(range(1, 20, 2))

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    for numbers in odd_value:
        print(f"Odd number: {numbers}")

if chapter_request == '4-7':

    # Enter exercise variables below.
    multiples_of_3 = list(range(3, 31, 3))

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    print(multiples_of_3)

if chapter_request == '4-8':

    # Enter exercise variables below
    
    # Wait Period
    input(f"\nPress enter to continue...\n")
    
    # Enter exercise code below.
    cubes = []
    for number in range(1, 11):
            cube = number**3
            cubes.append(cube)
    for cube in cubes:
        print(cube)

if chapter_request == '4-9':

    # Enter exercise variables below.
    list_comp = [numbers**3 for numbers in range(1, 11)]

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    print(list_comp)

if chapter_request == '4-10':

    # Enter exercise variables below.
    value = list(range(1, 1000001))
    middle = len(value) // 2
    middle_slice = value[middle-1:middle+2]
    first_3 = value[:2]
    last_3 = value[-2:]

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    print(f"First 3: {first_3}")
    print(f"Last 3: {last_3}")
    print(f"Middle 3: {middle_slice}")

if chapter_request == '4-11':

    # Enter exercise variables below.
    pizzas = ['pepperoni', 'sausage', 'meatlovers', 'supreme']
    friend_pizzas = pizzas[:]

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    pizzas.append('hawaiian')
    friend_pizzas.append("cheese")
    print(pizzas)
    print(friend_pizzas)
    
if chapter_request == '4-13':

    # Enter exercise variables below.
    buffet_foods = ('fried rice', 'egg rolls', 'chicken', 'beef', 'pork')

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    # Display the menu once
    print(f'Server: "Here are our menu items: {buffet_foods}. What would you like?"')
    user_selection = input()
    print(f"You have selected: {user_selection}")
    
    # Check if the selection is in thecccccbvnrtfferehbjv menu (case-insensitive)
    if user_selection.lower() in [food.lower() for food in buffet_foods]:
        print(f"Server: Great choice! I'll get that right out to you.")
    else:
        print(f"Sorry, that is not an option we have here.")
            
              

else:
    print(f"\nUnable to proceed. chapter_request not found.\n")