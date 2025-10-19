chapter_exercise = {

}

print(f"\nHello user. What chapter exercise are you on? Here are the available chapters:")
for key,value in chapter_exercise.items():
    print(f"\n{key}: {value}")
chapter_request = input(f"\n")

if chapter_request in chapter_exercise:
    print(f"\nGreat! You're working on chapter {chapter_request}.")
else:
    print(f"Chapter {chapter_request} is not in the list.")
    chapter_exercise.append(chapter_request)

# IF STATEMENT
if chapter_request == '':

    # Enter exercise variables below.

    # Wait Period
    input(f"\nPress enter to continue...\n")

    # Enter exercise code below.
   

# ERROR CHECK
else:
    print(f"\nUnable to proceed. chapter_request not found.\n")