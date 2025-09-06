chapter_exercise = ['3-4', '3-5', '3-6', '3-7', '3-8', '3-9', '3-10']
print(f"Hello user. What chapter exercise are you on? Here are the available chapters: {chapter_exercise}")
chapter_request = input()

if chapter_request in chapter_exercise:
    print(f"Great! You're working on chapter {chapter_request}.")
else:
    print(f"Chapter {chapter_request} is not in the list.")
    chapter_exercise.append(chapter_request)

if chapter_request == '3-4':
    print("You are now working on 3-4")
    wait = input("Press enter to continue...")
    print("3-4. Guest List:\nIf you could invite anyone, living or deceased, to dinner, who would you invite?\n" \
    "Make a list that includes at least three people youd like to invite to dinner.\n" \
    "Then use your list to print a message to each person, inviting them to dinner.\n")

    # Enter exercise code below.

    guest_list = ['Abraham Lincoln', 'George Washington', 'Barack Obama']
    for guest in guest_list:
        print(f"Dear {guest}, you are invited to dinner.")

if chapter_request == '3-5':
    
    # Enter exercise variables below.
    exercise_question = "3-5. Change Guest List:\nYou just found out that your favorite guest can't make it to dinner.\n" \
    "Modify your guest list, replacing the unavailable guest with a new one.\n"
    guest_list = ['Abraham Lincoln', 'George Washington', 'Barack Obama']

    # Wait Period
    wait = input("Press enter to continue...")
    print(exercise_question)

    # Enter exercise code below.
    print(guest_list)
    print(f"\nUnfortunately, {guest_list[2]} can't make it to dinner.\n")
    guest_list[2] = 'Michelle Obama'
    for guest in guest_list:
        print(f"Dear {guest}, you are invited to dinner.")

if chapter_request == '3-6':

    # Enter exercise variables below.
    exercise_question = "3-6. More Guests:\nYou just found out that you can invite more people to dinner.\n" \
    "Add a new guest to your list.\n"
    guest_list = ['Abraham Lincoln', 'George Washington', 'Barack Obama']

    # Wait Period
    wait = input(f"Press enter to continue...\n")
    print(exercise_question)
    # Enter exercise code below.
    print(f"Current Guest List: {guest_list}")
    print("\nGood news! We can invite more people to dinner.\n")
    guest_list.insert(0, 'Martin Luther King Jr.')
    guest_list.insert(2, 'Thomas Jefferson')
    guest_list.append('Joe Biden')
    for guest in guest_list:
        print(f"Dear {guest}, you are invited to dinner.")

if chapter_request == '3-7':

    # Enter exercise variables below.
    exercise_question = "3-7. Shrinking Guest List:\nYou just found out that you have to reduce your guest list.\n" \
    "Remove guests from your list until you have only two left.\n"
    guest_list = ['Abraham Lincoln', 'George Washington', 'Barack Obama']

    # Wait Period
    wait = input(f"Press enter to continue...\n")
    print(exercise_question)

    # Enter exercise code below.
    print(f"Current Guest List: {guest_list}")
    print("\nBad news! We can only invite two people to dinner.\n")
    while len(guest_list) > 2:
        removed_guest = guest_list.pop()
        print(f"Sorry {removed_guest}, you can't come to dinner.")
    for guest in guest_list:
        print(f"Dear {guest}, you are still invited to dinner.")

if chapter_request == '3-8':
    # Enter exercise variables below.
    exercise_question = "3-8. Seeing the World:\nThink of at least five places in the world you’d like to visit.\n" \
    "Store the locations in a list. Make sure the list is not in alphabetical order.\n"
    places = ['Japan', 'Korea', 'Vietnam', 'Switzerland']

    # Wait Period
    wait = input(f"Press enter to continue...\n")
    print(exercise_question)
    
    # Enter exercise code below.
    print(f"Original list: {places}")
    print(f"\nAlphabetical order: {sorted(places)}")
    print(f"\nOriginal list again: {places}")
    print(f"\nReverse alphabetical order: {sorted(places, reverse=True)}")
    print(f"\nOriginal list again: {places}")
    places.reverse()
    print(f"\nReversed list: {places}")
    places.reverse()
    print(f"\nOriginal list again: {places}")
    places.sort()
    print(f"\nPermanently sorted list: {places}")
    places.sort(reverse=True)
    print(f"\nPermanently sorted in reverse alphabetical order: {places}")

if chapter_request == '3-9':
    # Enter exercise variables below.
    guest_list = ['Abraham Lincoln', 'George Washington', 'Barack Obama', 'Eisenhower', 'John F. Kennedy']

    # Wait Period
    wait = input(f"Press enter to continue...\n")
    print(exercise_question)
    
    # Enter exercise code below.
    print(f"Current Guest List: {guest_list}")
    print(f"Total number of guests: {len(guest_list)}")
