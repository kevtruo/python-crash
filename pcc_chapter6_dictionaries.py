chapter_exercise = {
    '6.0': 'Custom Exercise',
    '6.1': 'Person',
    '6.2': 'Favorite Numbers',
    '6.3': 'Glossary',
    '6.3.5': 'Changing Positions',
    '6.4': "Glossary 2",
    '6.5': "Rivers",
    '6.6': "Polling",
    '6.6.5': "Nesting Lists in Dictionaries",
    '6.7': "People",
    '6.8': "Pets",
    '6.9': 'Favorite Places',
    '6.11': 'Cities',
}
print(f"\nHello user. What chapter exercise are you on? Here are the available chapters:")
for key,value in chapter_exercise.items():
    print(f"\n{key}: {value}")
chapter_request = input(f"\nChapter Exercise being worked on: ")

if chapter_request in chapter_exercise:
    print(f"\nGreat! You're working on chapter: {chapter_request} - {chapter_exercise[chapter_request]}.")
else:
    print(f"Chapter {chapter_request} is not in the list.")
    chapter_exercise.append(chapter_request)

if chapter_request == '6.0':

    # Enter exercise variables below.
    target = {}
    ally = {}

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    target['color'] = 'green'
    target['faction'] = 'argonauts'
    target['class'] = 'frigate'
    print(f"Target info: {target}\nHappy hunting.")
    input(f"\nPress enter to proceed.")
    kill = input(f"Who did you shoot down:")
    
if chapter_request == '6.1':

    # Enter exercise variables below.
    kaden = {'first_name': 'kaden', 'last_name': 'duong', 'age': '19', 'city': '19',}
  

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    print(f"Printing Kaden's first name: {kaden['first_name']}")
    print(f"Printing Kaden's last name: {kaden['last_name']}")
    print(f"Printing Kaden's age: {kaden['age']}")
    print(f"Printing Kaden's city: {kaden['city']}")
   
if chapter_request == '6.2':

    # Enter exercise variables below.
    favorite_number = {
        'Jae': '9',
        'Naing': '9',
        'Jaren': '10',
        'Matt': '4'
    }

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    print(favorite_number['Jae'])
    print(favorite_number['Naing'])

if chapter_request == '6.3':

    # Enter exercise variables below.
    programming_words = {
        'List': 'A collection of items in a particular order.',
        'Dictionary': 'A collection of key-value pairs.',
        'Key-value': 'A set of values associated with a key in a dictionary.',
        'If statements': 'Conditional statements that run code only when certain conditions are true.'
    }

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    print(f"A list is a: {programming_words['List']}")
    print(f"A dictionary is a: {programming_words['Dictionary']}")
    print(f"A key-value is a: {programming_words['Key-value']}")
    print(f"An if statement is a: {programming_words['If statements']}")

if chapter_request == '6.3.5':

    # Enter exercise variables below.

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
    print(f"Original position: {alien_0['x_position']}")

    if alien_0['speed'] == 'slow':
        x_increment = 1
    elif alien_0['speed'] == 'medium':
        x_increment = 2
    else:
        x_increment = 3

    alien_0['x_position'] = alien_0['x_position'] + x_increment

    print(f"New position: {alien_0['x_position']}")

if chapter_request == '6.4':

    # Enter exercise variables below.
    programming_words = {
        'List': 'A collection of items in a particular order.',
        'Dictionary': 'A collection of key-value pairs.',
        'Key-value': 'A set of values associated with a key in a dictionary.',
        'If statements': 'Conditional statements that run code only when certain conditions are true.'
    }

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    for term in programming_words:
        print(term)
    print(f"\n")
    for definitions in programming_words:
        print(definitions)

if chapter_request == '6.5':

    # Enter exercise variables below.
    rivers = {
        'nile': 'egypt',
        'danube': 'germany',
        'thames': 'england',
        'seine': 'france'
    }

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    for river, country in rivers.items():
        print(f"The {river.title()} runs through {country.title()}.")
    print(f"\n")
    for river_name in rivers:
        print(river_name)
    print(f'\n')
    for river_country in rivers.values():
        print(river_country)

if chapter_request == '6.6':

    # Enter exercise variables below.
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    
    # List of people who should take the poll (mix of existing and new names)
    people_to_poll = ['jen', 'sarah', 'mike', 'alice', 'edward', 'bob', 'phil', 'lisa']

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    for person in people_to_poll:
        if person in favorite_languages:
            print(f"Thank you, {person.title()}, for responding to the poll!")
        else:
            print(f"Hi {person.title()}, please take our favorite languages poll!")

if chapter_request == '6.6.5':

    # Enter exercise variables below.
    favorite_languages = {
        'jen': ['python','c','go'],
        'sarah': ['c','java'],
        'edward': ['ruby'],
        'phil': ['python'],
    }

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    for name in favorite_languages:
        print(f"\n{name.title()}'s favorite programming language(s) are:")
        for language in favorite_languages[name]:
            print(f"\t- {language.title()}")

if chapter_request == '6.7':

    # Enter exercise variables below.
    people = {
        'kaden': {
            'first_name': 'kaden', 
            'last_name': 'duong', 
            'age': '19', 
            'city': 'tampa',
        },

        'kem': {
            'first_name': 'kem',
            'last_name': 'decamp',
            'age': '26',
            'city': 'apopka'
        },

        'kellie': {
            'first_name': 'kellie',
            'last_name': 'duong',
            'age': '25',
            'city': 'tampa',
        },
    }
    
    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    for user, user_details in people.items():
        full_name = f"{user_details['first_name']} {user_details['last_name']}"
        print(f"Username: {user.title()}")
        print(f"\tFull name: {full_name.title()}")
        print(f"\tUser Location: {user_details['city'].title()}")

if chapter_request == '6.8':

    # Enter exercise variables below.
    pets = [
        {
            'name': 'rocky',
            'species': 'dog', 
            'breed': 'english bulldog', 
            'age': '9', 
            'owner': 'kellie',
        },

        {
            'name': 'poppy',
            'species': 'dog',
            'breed': 'english bulldog',
            'age': '5',
            'owner': 'kaden'
        },

        {
            'name': 'nala',
            'species': 'cat',
            'breed': 'domestic',
            'age': '7',
            'owner': 'kem',
        },
    ]
    
    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    for pet in pets:
        print(f"Pet Name: {pet['name'].title()}")
        print(f"\tSpecies: {pet['species'].title()}")
        print(f"\tBreed: {pet['breed'].title()}")
        print(f"\tAge: {pet['age']} years old")
        print(f"\tOwner: {pet['owner'].title()}")
        print()  # Blank line between pets

if chapter_request == '6.9':

    # Enter exercise variables below.
    favorite_places = {
        'Jim': ['Tokyo','London','Berlin'],
        'Bob': ['Atlanta','Chicago'],
        'Alice': ['Tampa','New York','Miami'],
    }

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
    for person, places in favorite_places.items():
        print(f"{person}'s favorite places are:")
        for place in places:
            print(f"\t- {place}")
        print()  # Blank line between people

if chapter_request == '6.11':

    # Enter exercise variables below.
    cities = (
        'Los Angeles': (
            'State': 'California',
            'Country': 'United States',
            'Continent': 'North America',
        ),
        'New York':  (
            'State': 'New York',
            'Country': 'United States',
            'Continent': 'North America',
        ),
        'Montreal': (
            'State': 'Quebec',
            'Country': 'Canada',
            'Continent': 'North America',
        )
    )

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.

# ERROR CHECK
else:
    print(f"\nUnable to proceed. chapter_request not found.\n")