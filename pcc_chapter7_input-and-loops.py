chapter_exercise = {
    '7.1': 'Rental Car',
    '7.2': 'Restaurant Seating',
    '7.2.5': 'Favorite City',
    '7.4': 'Pizza Toppings',
    '7.5': 'Movie Tickets',
    '7.6': 'Three Exits',
}

print(f"\nHello user. Welcome to chapter 7! What chapter exercise are you on? Here are the available chapters:")
for key,value in chapter_exercise.items():
    print(f"\n{key}: {value}")
chapter_request = input(f"\nChapter Exercise being worked on: ")

if chapter_request in chapter_exercise:
    print(f"\nGreat! You're working on chapter: {chapter_request} - {chapter_exercise[chapter_request]}.")
else:
    print(f"Chapter {chapter_request} is not in the list.")
    chapter_exercise.append(chapter_request)

if chapter_request == '7.1':
    input(f"\nPress enter to continue...\n")

    make = input(f"What kind of car would you like to rent? ")

    print(f"Let me see if I can find a {make} for you.")

if chapter_request == '7.2':
    input(f"\nPress enter to continue...\n")

    guest_number = input(f"How many guests are in your group? ")
    int_guest_number = int(guest_number)
    if int_guest_number >= 8:
        print(f"This is a large group! Please wait as we get you accomodated.")
    else:
        print(f"We will seat you now, please come with me.")

if chapter_request == '7.2.5':
    input(f"\nPress enter to continue...\n")

    prompt = "\nPlease enter the name of a city you would like to visit: "
    prompt += "\n(Enter 'quit' when you are finished.) "

    travel_list = []
    while True:
        city = input(prompt)

        if city == 'quit':
            break
        else:
            travel_list.append(city)
            print(f"Adding city to your travel list...")

    print(f"Your current travel list is {travel_list}!")

if chapter_request == '7.4':
    input(f"\nPress enter to continue...\n")

    pizza_order = [ ]
    print(f"Welcome to KT's Pizza!\n")

    while True:
        pizza_topping = input(f"Please enter what pizza topping you'd like: ")
        pizza_order.append(pizza_topping)
        print(f"Adding {pizza_topping.upper()} to your pizza!")

        continue_order = input(f"Would you like to add anymore toppings? (y/n): ")
        if continue_order.lower() != 'y':
            break
    
    print(f"\nYour final pizza order includes: {pizza_order}")
    print(f"Total toppings: {len(pizza_order)}")

if chapter_request == '7.5':
    input(f"\nPress enter to continue...\n")
    
    print(f"Welcome to KT Movies!\n")

    while True:
        age_input = input(f"Enter your age (or 'quit' to exit): ")
        
        if age_input.lower() == 'quit':
            break
        
        user_age = int(age_input)
        
        if user_age < 3:
            print(f"Your ticket is free!")
        elif user_age <= 12:
            print(f"Your ticket is $10.")
        else:
            print(f"Your ticket is $15.")
        
        print()
    
    print(f"Thank you for visiting KT Movies!")

if chapter_request == '7.6':
    input(f"\nPress enter to continue...\n")

    print(f"Welcome to KT's Firearms!\n")
    purchase_order = input(f"\nAre you here to purchase a firearm? (y/n): ")

    while purchase_order == 'y':
        print(f"Customers purchasing firearms must enter their age.")
        age_input = input(f"Enter your age (or 'quit' to exit): ")
        
        if age_input.lower() == 'quit':
            print(f"\nThank you for visiting KT's Firearms.\n")
            break
        
        user_age = int(age_input)
        if user_age < 18:
            print(f"Sorry, you are not permitted to purchase firearms.")
            break
        elif user_age < 21:
            print(f"You may purchase firearms, but no handguns.")
        else:
            print(f"Your may purchase any kind of firearm.")

    while purchase_order == 'n':
        print(f"\nThank you for visiting KT's Firearms.\n")
        break

# ERROR CHECK
else:
    print(f"\nUnable to proceed. chapter_request not found.\n")