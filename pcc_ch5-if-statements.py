chapter_exercise = ['5-1','5-3','5-6','5-8','5-9','5-10']
print(f"Hello user. What chapter exercise are you on? Here are the available chapters: {chapter_exercise}")
chapter_request = input()

if chapter_request in chapter_exercise:
    print(f"\nGreat! You're working on chapter {chapter_request}.")
else:
    print(f"Chapter {chapter_request} is not in the list.")
    chapter_exercise.append(chapter_request)

if chapter_request == '5-1':

    # Enter exercise variables below.
    car1 = 'subaru'
    car2 = 'toyota'
    x = 10
    y = 20

    car_notequal = car1 != car2 #TRUE
    car_equal = car1 == car2 #FALSE
    car_subaru = car1 == 'subaru' #TRUE
    car_notsubaru = car1 == 'mazda' #FALSE
    car_toyota = car2 == 'toyota' #TRUE
    car_nottoyota = car2 == 'honda' #FALSE
    xy_greater = x > y #FALSE
    xy_lesser = x < y #TRUE
    xy_greater_equal = x >= y #FALSE
    xy_lesser_equal = x <= y #TRUE



    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    ## Boolean values, 10 T 10 F.
    print(f"car1 and car2 are not equal: {car_notequal}")
    print(f"car1 and car2 are equal: {car_equal}")
    print(f"car1 is equal to 'subaru': {car_subaru}")
    print(f"car1 is equal to 'mazda': {car_notsubaru}")
    print(f"car2 is equal to 'toyota': {car_toyota}")
    print(f"car2 is equal to 'honda': {car_nottoyota}")
    print(f"x is greater than y: {xy_greater}")
    print(f"x is less than y: {xy_lesser}")
    print(f"x is greater than or equal to y: {xy_greater_equal}")
    print(f"x is less than or equal to y: {xy_lesser_equal}")

if chapter_request == '5-3':

    # Enter exercise variables below.
    alien_colors = ['green', 'blue', 'red']

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    print(f"What color alien did you shoot down?")
    player_kill = input()
    if player_kill == 'green':
        print(f"You shot down an ally!")
    elif player_kill == 'blue':
        print(f"You shot down one of us!")
    elif player_kill == 'red':
        print(f"Nice shooting!")

if chapter_request == '5-8':

    # Enter exercise variables below.
    usernames = ['Kaden','Kellie','Kevin','admin']

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    username_entry = input("Username: ")
    if username_entry == 'admin':
        print(f"Hello admin.")
    else:
        print(f"Hello user.")

if chapter_request == '5-9':

    # Enter exercise variables below.
    usernames = []

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    if usernames:
        username_entry = input("Username: ")
        if username_entry == 'admin':
            print(f"Hello admin.")
        else:
            print(f"Hello user.")
    else:
        print(f"No users found.\n")

if chapter_request == '5-10':

    # Enter exercise variables below.
    current_users = ['Kevin','Alfred','Rohan','Tyler']
    new_users = ['Rohan','Alfred']

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    user_input = input("Username: ")
    user_lower = user_input.lower()
    current_users_lower = [user.lower() for user in current_users]
    
    if user_lower in current_users_lower:
        print(f"That username is unavailable. Please enter another one.")
    else:
        print(f"Username '{user_input}' is available!")


# ERROR CHECK
else:
    print(f"\nUnable to proceed. chapter_request not found.\n")
    